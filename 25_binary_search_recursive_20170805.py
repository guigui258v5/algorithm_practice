def binary_search(alist, item):  # alist必须是有序的
    # print(alist)
    n = len(alist)
    if n < 1:
        return False

    mid = n//2
    # print(alist[mid])
    # print(item)
    if item == alist[mid]:
        return True
    elif item < alist[mid]:
        return binary_search(alist[:mid], item)  # 务必return,否则里面判断出来的True不能传递出来
    elif item > alist[mid]:
        return binary_search(alist[mid+1:], item)

if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(l ,8))
    print(binary_search(l ,10))
