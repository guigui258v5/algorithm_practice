def merge_sort(l):
    # 对列表进行二分分解
    n = len(l)
    if n <= 1:
        return l
    mid_posi = n//2
    # print(1)
    l_list = merge_sort(l[:mid_posi])
    # print(2)
    r_list = merge_sort(l[mid_posi:])
    # print(3)

    # 对列表进行合并
    sorted_list = []
    l_posi = 0
    r_posi = 0
    # print('l_list: %s' % l_list)
    # print('r_list: %s' % r_list)

    while l_posi < len(l_list) and r_posi < len(l_list):
        if l_list[l_posi] <= r_list[r_posi]:
            sorted_list.append(l_list[l_posi])
            l_posi += 1
        else:
            sorted_list.append(r_list[r_posi])
            r_posi += 1

    # 将列表剩余部分合并
    sorted_list += l_list[l_posi:]
    sorted_list += r_list[r_posi:]
    # print('sorted_list: %s' % sorted_list)

    return sorted_list


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    sorted_list = merge_sort(l)
    print(sorted_list)
