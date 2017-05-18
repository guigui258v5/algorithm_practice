def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    l = [6, 2, 1, 8, 3, 5, 0, 4, 9, 7]
    print(l)
    bubble_sort(l)
    print(l)
