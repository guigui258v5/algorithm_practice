def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


if __name__ == '__main__':
    l = [6, 2, 1, 8, 3, 5, 0, 4, 9, 7]
    print(l)
    insert_sort(l)
    print(l)
