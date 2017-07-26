def insert_sort(l):
    n = len(l)
    # 要排序的元素
    for i in range(1, n):
        # 已排序的元素
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    insert_sort(l)
    print(l)
