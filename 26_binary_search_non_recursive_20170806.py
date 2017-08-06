def binary_search(alist, item):
    n = len(alist)
    l_posi = 0
    r_posi = n-1

    while l_posi <= r_posi:
        mid = (l_posi+r_posi)//2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            r_posi = mid-1
        elif item > alist[mid]:
            l_posi = mid+1
    return False

if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(l ,8))
    print(binary_search(l ,10))