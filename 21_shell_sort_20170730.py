def shell_sort(l):
    n = len(l)
    # 初始间隔
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap-1, -gap):
                if l[j] < l[j-gap]:
                    l[j], l[j-gap] = l[j-gap], l[j]
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    shell_sort(l)
    print(l)
