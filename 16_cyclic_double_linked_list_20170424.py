class ListValueError(ValueError):
    pass


class ListTypeError(TypeError):
    pass


class Node(object):
    """结点 类"""
    def __init__(self, elem, llink=None, rlink=None):
        self.elem = elem
        self.llink = llink
        self.rlink = rlink


class CyclicDoubleLinkedList(object):
    """双向循环链表 类"""
    def __init__(self, head=None, rear=None):
        self.__head = head
        self.__rear = rear

    def is_empty(self):
        return not self.__head

    def length(self):
        n = 0
        if self.is_empty():
            return n
        pointer = self.__head
        while pointer.rlink != self.__head:
            n += 1
            pointer = pointer.rlink
        n += 1
        return n

    def travel(self):
        result = ''
        if self.is_empty():
            return result
        pointer = self.__head
        while pointer.rlink != self.__head:
            result += str(pointer.elem) + ' '
            pointer = pointer.rlink
        result += str(pointer.elem)
        return result

    def first_add(self, elem):
        """在最前面插入"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            self.__rear = node
            return
        node.rlink, node.llink = self.__head, self.__rear
        self.__rear.rlink = node
        self.__head.llink = node
        self.__head = node

    def last_add(self, elem):
        """在最后面插入"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            self.__rear = node
            return
        node.llink, node.rlink = self.__rear, self.__head
        self.__rear.rlink = node
        self.__head.llink = node
        self.__rear = node

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
        node.llink, node.rlink = pointer, pointer.rlink
        pointer.rlink.llink = node
        pointer.rlink = node

    def first_del(self):
        if self.is_empty():
            raise ListValueError()
        if self.__head == self.__rear:
            self.__head = None
            self.__rear = None
            return
        self.__rear.rlink = self.__head.rlink
        self.__head.rlink.llink = self.__rear
        self.__head = self.__head.rlink

    def last_del(self):
        if self.is_empty():
            raise ListValueError()
        if self.__head == self.__rear:
            self.__head = None
            self.__rear = None
            return
        self.__head.llink = self.__rear.llink
        self.__rear.llink.rlink = self.__head
        self.__rear = self.__rear.llink

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
        pointer.rlink.rlink.llink = pointer
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
        while pointer != self.__rear:
            op(pointer.elem)
            pointer = pointer.rlink
        op(pointer.elem)

if __name__ == '__main__':
    cdll = CyclicDoubleLinkedList()
    print('-----is_empty-----')
    print(cdll.is_empty())

    print('-----first_add, last_add, travel, length-----')
    cdll.first_add(1)
    cdll.first_add(2)
    cdll.last_add(3)
    cdll.last_add(4)
    print(cdll.travel())  # [2, 1, 3, 4]
    print(cdll.length())  # 4
    print(cdll.is_empty())

    print('-----middle_add-----')
    cdll.middle_add(1, 5)
    print(cdll.travel())  # [2, 5, 1, 3, 4]
    cdll.middle_add(-5, 6)
    print(cdll.travel())  # [6, 2, 5, 1, 3, 4]
    cdll.middle_add(-100, 7)
    print(cdll.travel())  # [7, 6, 2, 5, 1, 3, 4]
    cdll.middle_add(100, 8)
    print(cdll.travel())  # [7, 6, 2, 5, 1, 3, 4, 8]
    print(cdll.length())  # 8

    print('-----first_del, last_del-----')
    cdll.first_del()
    print(cdll.travel())  # [6, 2, 5, 1, 3, 4, 8]
    cdll.last_del()
    print(cdll.travel())  # [6, 2, 5, 1, 3, 4]

    print('-----middle_del-----')
    cdll.middle_del(2)
    print(cdll.travel())  # [6, 2, 1, 3, 4]
    cdll.middle_del(-100)
    print(cdll.travel())  # [2, 1, 3, 4]
    cdll.middle_del(100)
    print(cdll.travel())  # [2, 1, 3]
    cdll.middle_del(100)
    print(cdll.travel())  # [2, 1]
    cdll.middle_del(100)
    print(cdll.travel())  # [2]
    cdll.first_del()
    print(cdll.travel())  # []

    print('-----find-----')
    cdll.last_add(1)
    cdll.last_add(2)
    cdll.last_add(3)
    cdll.last_add(4)
    cdll.last_add(5)
    cdll.last_add(6)
    print(cdll.travel())  # [1, 2, 3, 4, 5, 6]
    print(cdll.find(7))  # -1
    print(cdll.find(6))  # 5
    print(cdll.find(1))  # 0

    print('-----for_each-----')
    cdll.for_each(print)
