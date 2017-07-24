def bubble_sort(l):
    n = len(l)
    for j in range(n-1):
        # 用于判断此轮遍历过程中各元素之间的位置是否发生了改变
        for i in range(n-1-j):
            if l[i] > l[i+1]:
                l[i+1], l[i] = l[i], l[i+1]


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    bubble_sort(l)
    print(l)
