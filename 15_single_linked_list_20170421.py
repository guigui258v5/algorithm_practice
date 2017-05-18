class ListValueError(ValueError):
    pass


class ListTypeError(TypeError):
    pass


class Node(object):
    """结点 类"""
    def __init__(self, elem, rlink=None):
        self.elem = elem
        self.rlink = rlink


class SingleLinkedList(object):
    """单链表 类"""
    def __init__(self, head=None):
        self.__head = head


    def get_head(self):
        return self.__head

    def is_empty(self):
        return not self.__head

    def length(self):
        """单链表长度"""
        n = 0
        if not self.__head:
            return n
        pointer = self.__head
        while pointer.rlink:
            n += 1
            pointer = pointer.rlink
        n += 1
        return n

    def travel(self):
        result = ''
        if not self.__head:
            return result
        pointer = self.__head
        while pointer.rlink:
            result += str(pointer.elem) + ' '
            pointer = pointer.rlink
        result += str(pointer.elem)
        return result

    def first_add(self, elem):
        """在最前面插入"""
        node = Node(elem)
        if not self.__head:
            self.__head = node
            return
        self.__head, node.rlink = node, self.__head

    def last_add(self, elem):
        """在最后面插入"""
        node = Node(elem)
        if not self.__head:
            self.__head = node
            return
        pointer = self.__head
        while pointer.rlink:
            pointer = pointer.rlink
        pointer.rlink = node

    def middle_add(self, index, elem):
        node = Node(elem)
        n = self.length()
        if index < 0:
            index += n
        if index <= 0:
            self.first_add(elem)
            return
        if index >= n:
            self.last_add(elem)
            return
        pointer = self.__head
        for i in range(index-1):
            pointer = pointer.rlink
        pointer.rlink, node.rlink = node, pointer.rlink

    def first_del(self):
        if self.is_empty():
            raise ListValueError()
        self.__head = self.__head.rlink

    def last_del(self):
        if self.is_empty():
            raise ListValueError()
        pointer = self.__head
        if not self.__head.rlink:
            self.__head = None
            return
        while pointer.rlink.rlink:
            pointer = pointer.rlink
        pointer.rlink = None

    def middle_del(self, index):
        if self.is_empty():
            raise ListValueError()
        n = self.length()
        if index < 0:
            index += n
        if index <= 0:
            self.first_del()
            return
        if index >= n:
            self.last_del()
            return
        pointer = self.__head
        for i in range(index-1):
            pointer = pointer.rlink
        pointer.rlink = pointer.rlink.rlink

    def find(self, elem):
        if self.is_empty():
            raise ListValueError()
        n = self.length()
        pointer = self.__head
        for i in range(n):
            if pointer.elem == elem:
                return i
            pointer = pointer.rlink
        return -1

    def for_each(self, op):
        """所有结点的元素进行操作"""
        if self.is_empty():
            return
        pointer = self.__head
        while pointer:
            op(pointer.elem)
            pointer = pointer.rlink

    def rev(self):
        """反转链表 第一种方法"""
        if self.is_empty():
            return
        p = self.__head
        q = SingleLinkedList()
        while p.rlink:
            q.first_add(p.elem)
            p = p.rlink
        q.first_add(p.elem)
        self.__head = q.get_head()

    # def rev(self):
    #     """反转链表 第二种方法 ??????"""
    #     p = None
    #     while not self.__head:
    #         q = self.__head
    #         self.__head = q.rlink
    #         q.rlink = p
    #         p = q
    #     self.__head = p

if __name__ == '__main__':
    sll = SingleLinkedList()
    print('-----is_empty-----')
    print(sll.is_empty())

    print('-----first_add, last_add, travel, length-----')
    sll.first_add(1)
    sll.first_add(2)
    sll.last_add(3)
    sll.last_add(4)
    print(sll.travel())  # [2, 1, 3, 4]
    print(sll.length())  # 4
    print(sll.is_empty())

    print('-----middle_add-----')
    sll.middle_add(1, 5)
    print(sll.travel())  # [2, 5, 1, 3, 4]
    sll.middle_add(-5, 6)
    print(sll.travel())  # [6, 2, 5, 1, 3, 4]
    sll.middle_add(-100, 7)
    print(sll.travel())  # [7, 6, 2, 5, 1, 3, 4]
    sll.middle_add(100, 8)
    print(sll.travel())  # [7, 6, 2, 5, 1, 3, 4, 8]
    print(sll.length())  # 8

    print('-----first_del, last_del-----')
    sll.first_del()
    print(sll.travel())  # [6, 2, 5, 1, 3, 4, 8]
    sll.last_del()
    print(sll.travel())  # [6, 2, 5, 1, 3, 4]

    print('-----middle_del-----')
    sll.middle_del(2)
    print(sll.travel())  # [6, 2, 1, 3, 4]
    sll.middle_del(-100)
    print(sll.travel())  # [2, 1, 3, 4]
    sll.middle_del(100)
    print(sll.travel())  # [2, 1, 3]
    sll.middle_del(100)
    print(sll.travel())  # [2, 1]
    sll.middle_del(100)
    print(sll.travel())  # [2]
    sll.first_del()
    print(sll.travel())  # []

    print('-----find-----')
    sll.last_add(1)
    sll.last_add(2)
    sll.last_add(3)
    sll.last_add(4)
    sll.last_add(5)
    sll.last_add(6)
    print(sll.find(7))  # -1
    print(sll.find(6))  # 5
    print(sll.find(1))  # 0
    print('-----for_each-----')
    sll.for_each(print)
    print('-----rev-----')
    sll.rev()
    sll.for_each(print)
