def binary_search(alist, item):
    n = len(alist)
    if n < 1:
        return False
    mid_posi = (n-1)//2

    if item < alist[mid_posi]:
        return binary_search(alist[:mid_posi], item)
    elif item > alist[mid_posi]:
        return binary_search(alist[mid_posi+1:], item)
    elif item == alist[mid_posi]:
        return True


if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(l, 0))
    print(binary_search(l, 1))
    print(binary_search(l, 2))
    print(binary_search(l, 3))
    print(binary_search(l, 4))
    print(binary_search(l, 5))
    print(binary_search(l, 6))
    print(binary_search(l, 7))
    print(binary_search(l, 8))
    print(binary_search(l, 9))
    print(binary_search(l, 10))
