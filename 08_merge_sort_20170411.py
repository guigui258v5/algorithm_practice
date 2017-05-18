def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid_posi = n//2
    llist = merge_sort(alist[:mid_posi])
    rlist = merge_sort(alist[mid_posi:])

    lposi = 0
    rposi = 0
    sorted_list = []
    # print('llist', llist)
    # print('rlist', rlist)
    while lposi < len(llist) and rposi < len(llist):
        if llist[lposi] <= rlist[rposi]:
            sorted_list.append(llist[lposi])
            lposi += 1
        else:
            sorted_list.append(rlist[rposi])
            rposi += 1

    sorted_list += llist[lposi:]
    sorted_list += rlist[rposi:]
    # print('sorted_list', sorted_list)

    return sorted_list


if __name__ == '__main__':
    l = [6, 2, 1, 8, 3, 5, 0, 4, 7, 9]
    print(l)
    result = merge_sort(l)
    print(result)
