class Node(object):
    def __init__(self, elem, llink=None, rlink=None):
        self.elem = elem
        self.llink = llink
        self.rlink = rlink


class DoubleLinkList(object):
    def __init__(self, head=None):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def length(self):
        n = 0
        ref = self.__head
        while ref:
            ref = ref.rlink
            n += 1
        return n

    def add(self, elem):
        node = Node(elem)
        if self.__head is None:
            self.__head = node
            return
        node.rlink = self.__head
        self.__head.llink = node
        self.__head = node

    def append(self, elem):
        node = Node(elem)
        if self.__head is None:
            self.__head = node
            return
        ref = self.__head
        while ref.rlink:
            ref = ref.rlink
        ref.rlink = node
        node.llink = ref

    def insert(self, posi, elem):
        node = Node(elem)
        n = self.length()
        if posi >= n:
            self.append(elem)
            return
        if posi == 0 or posi+n <= 0:
            self.add(elem)
            return
        if posi < 0:
            posi = posi+n
        ref = self.__head
        for i in range(posi-1):
            ref = ref.rlink
        node.rlink = ref.rlink
        node.llink = ref
        ref.rlink.llink = node
        ref.rlink = node

    def travel(self):
        if self.__head is None:
            print('empty')
        ref = self.__head
        while ref:
            print(ref.elem, end=' ')
            ref = ref.rlink
        print('')

    def search(self, elem):
        ref = self.__head
        while ref:
            if ref.elem == elem:
                return True
            ref = ref.rlink
        return False

    def remove(self, elem):
        ref = self.__head
        if self.__head is None:
            print('无此节点')
            return

        if self.__head.elem == elem:
            self.__head = self.__head.rlink
            return

        while ref.rlink:
            if ref.rlink.elem == elem:
                ref.rlink = ref.rlink.rlink
                return
            ref = ref.rlink
        print('无此节点')


if __name__ == '__main__':
    dll = DoubleLinkList()

    print('-----1-----')
    print(dll.is_empty())  # True

    print('-----2-----')
    dll.travel()  # empty

    print('-----3-----')
    print(dll.length())  # 0

    print('-----4-----')
    dll.remove(3)  # 无此节点

    print('-----5-----')
    print(dll.search(1))  # False

    print('-----6-----')
    dll.add(1)
    dll.add(2)
    print(dll.search(1))  # True
    dll.travel()  # 2 1
    print(dll.is_empty())  # False
    print(dll.length())  # 2

    print('-----7-----')
    dll.append(3)
    dll.append(4)
    dll.travel()  # 2 1 3 4

    print('-----8-----')
    dll.insert(3, 5)
    dll.insert(-1, 6)
    dll.travel()  # 2 1 3 5 6 4

    print('-----9-----')
    dll.remove(2)  # 删除头端节点
    dll.travel()  # 1 3 5 6 4
    dll.remove(4)  # 删除尾端节点
    dll.travel()  # 1 3 5 6