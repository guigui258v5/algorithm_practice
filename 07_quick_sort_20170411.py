def quick_sort(alist, start, end):
    low = start
    high = end
    mid_value = alist[low]

    if start >= end:
        return

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)


if __name__ == '__main__':
    l = [6, 2, 1, 8, 3, 5, 0, 4, 9, 7]
    print(l)
    quick_sort(l, 0, len(l)-1)
    print(l)