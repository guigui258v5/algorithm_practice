def quick_sort(l, start, end):
    if start >= end:
        return

    low = start
    high = end
    mid_value = l[low]

    while low < high:
        # low<high这个条件必须在这里再次体现，避免出现循环过程中low>high的情况
        while low < high and l[high] >= mid_value:
            high -= 1
        # 当中间值右侧的值小于中间值时，将该值赋值于l[low](原来的值已保存至mid_value变量)
        l[low] = l[high]

        # low<high这个条件必须在这里再次体现，避免出现循环过程中low>high的情况
        while low < high and l[low] <= mid_value:
            low += 1
        # 当中间值左侧的值大于中间值时，将该值赋值于l[high](原来的值已保存至l[low])
        l[high] = l[low]

    # 退出循环时，说明low==high，则可以将mid_value的值赋予它
    l[low] = mid_value

    quick_sort(l, start, low-1)
    quick_sort(l, low+1, end)


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    quick_sort(l, 0, len(l)-1)
    print(l)
