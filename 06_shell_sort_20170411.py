def shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
        gap //= 2


if __name__ == '__main__':
    l = [6, 2, 1, 8, 3, 5, 0, 4, 9, 7]
    print(l)
    shell_sort(l)
    print(l)
