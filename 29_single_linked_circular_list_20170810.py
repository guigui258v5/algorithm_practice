class Node(object):
    def __init__(self, elem, link=None):
        self.elem = elem
        self.link = link


class SingleCyclinkedList(object):
    def __init__(self, head=None):
        self.__head = head
        if self.__head:
            self.next = self.__head

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        ref = self.__head
        n = 1
        while ref.link != self.__head:
            ref = ref.link
            n += 1
        return n

    def add(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.link = node
            return
        ref = self.__head
        while ref.link != self.__head:
            ref = ref.link
        ref.link = node
        node.link = self.__head
        self.__head = node

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.link = node
            return
        ref = self.__head
        while ref.link != self.__head:
            ref = ref.link
        ref.link = node
        node.link = self.__head

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
            ref = ref.link
        ref.link, node.link = node, ref.link

    def travel(self):
        if self.is_empty():
            print('empty')
            return
        ref = self.__head
        while ref.link != self.__head:
            print(ref.elem, end=' ')
            ref = ref.link
        print(ref.elem)

    def search(self, elem):
        if self.is_empty():
            return False
        ref = self.__head
        while ref.link != self.__head:
            if ref.elem == elem:
                return True
            ref = ref.link
        if ref.elem == elem:
            return True
        return False

    def remove(self, elem):
        ref = self.__head
        if self.__head is None:
            print('无此节点')
            return

        if self.__head.elem == elem:
            while ref.link != self.__head:
                ref = ref.link
            self.__head = self.__head.link
            ref.link = self.__head  # 将尾端节点接上新的头部
            return

        while ref.link != self.__head:
            if ref.link.elem == elem:
                ref.link = ref.link.link
                return
            ref = ref.link
        print('无此节点')


if __name__ == '__main__':
    scl = SingleCyclinkedList()

    print('-----1-----')
    print(scl.is_empty())  # True

    print('-----2-----')
    scl.travel()  # empty

    print('-----3-----')
    print(scl.length())  # 0

    print('-----4-----')
    scl.remove(3)  # 无此节点

    print('-----5-----')
    print(scl.search(1))  # False

    print('-----6-----')
    scl.add(1)
    scl.add(2)
    print(scl.search(1))  # True
    scl.travel()  # 2 1
    print(scl.is_empty())  # False
    print(scl.length())  # 2

    print('-----7-----')
    scl.append(3)
    scl.append(4)
    scl.travel()  # 2 1 3 4

    print('-----8-----')
    scl.insert(3, 5)
    scl.insert(-1, 6)
    scl.travel()  # 2 1 3 5 6 4

    print('-----9-----')
    scl.remove(2)  # 删除头端节点
    scl.travel()  # 1 3 5 6 4
    scl.remove(4)  # 删除尾端节点
    scl.travel()  # 1 3 5 6
