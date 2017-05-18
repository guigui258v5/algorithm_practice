def choice_sort(alist):
    n = len(alist)
    for i in range(n-1):
        for j in range(i+1, n):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]


if __name__ == '__main__':
    l = [6, 2, 1, 8, 3, 5, 0, 4, 9, 7]
    print(l)
    choice_sort(l)
    print(l)
