def select_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(i+1, n):
            # 一开始默认下标为i的值最小
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    select_sort(l)
    print(l)
