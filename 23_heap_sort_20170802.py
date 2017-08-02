def heap_sort(l):
    def max_heapify(root_index, end_index):
        """函数用于构造最大堆"""
        # 减一是因为堆的下标从１开始
        max_child_index = root_index*2-1

        # 在该二叉树有两个子节点的情况下，将两个子节点比较大小
        if max_child_index + 1 < end_index:
            if l[max_child_index+1] > l[max_child_index]:
                max_child_index += 1

        # 将最大的子节点与根节点做比较
        if l[max_child_index] > l[root_index-1]:
            l[max_child_index], l[root_index-1] = l[root_index-1], l[max_child_index]


    # 循环构造最大堆，而后将最大堆的根节点与末节点调换
    for end_index in range(len(l), 1, -1):
        # 每次要构造的最大堆大小与末节点有关
        max_root_index = end_index//2

        # 构造一个最大堆
        for root_index in range(max_root_index, 0, -1):
            max_heapify(root_index, end_index)

        # 将最大堆的根节点与末节点调换
        l[0], l[end_index-1] = l[end_index-1], l[0]


if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    heap_sort(l)
    print(l)