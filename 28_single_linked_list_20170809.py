class Node(object):
    def __init__(self, elem, link=None):
        self.elem = elem
        self.link = link


class SingleLinkList(object):
    def __init__(self, head=None):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def length(self):
        n = 0
        ref = self.__head
        while ref:
            ref = ref.link
            n += 1
        return n

    def add(self, elem):
        node = Node(elem)
        if self.__head is None:
            self.__head = node
            return
        self.__head, node.link = node, self.__head

    def append(self, elem):
        node = Node(elem)
        if self.__head is None:
            self.__head = node
            return
        ref = self.__head
        while ref.link:
            ref = ref.link
        ref.link = node

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
        if self.__head is None:
            print('empty')
        ref = self.__head
        while ref:
            print(ref.elem, end=' ')
            ref = ref.link
        print('')

    def search(self, elem):
        ref = self.__head
        while ref:
            if ref.elem == elem:
                return True
            ref = ref.link
        return False

    def remove(self, elem):
        ref = self.__head
        if self.__head is None:
            print('无此节点')
            return

        if self.__head.elem == elem:
            self.__head = self.__head.link
            return

        while ref.link:
            if ref.link.elem == elem:
                ref.link = ref.link.link
                return
            ref = ref.link
        print('无此节点')


if __name__ == '__main__':
    sll = SingleLinkList()

    print('-----1-----')
    print(sll.is_empty())  # True

    print('-----2-----')
    sll.travel()  # empty

    print('-----3-----')
    print(sll.length())  # 0

    print('-----4-----')
    sll.remove(3)  # 无此节点

    print('-----5-----')
    print(sll.search(1))  # False

    print('-----6-----')
    sll.add(1)
    sll.add(2)
    print(sll.search(1))  # True
    sll.travel()  # 2 1
    print(sll.is_empty())  # False
    print(sll.length())  # 2

    print('-----7-----')
    sll.append(3)
    sll.append(4)
    sll.travel()  # 2 1 3 4

    print('-----8-----')
    sll.insert(3, 5)
    sll.insert(-1, 6)
    sll.travel()  # 2 1 3 5 6 4

    print('-----9-----')
    sll.remove(2)  # 删除头端节点
    sll.travel()  # 1 3 5 6 4
    sll.remove(4)  # 删除尾端节点
    sll.travel()  # 1 3 5 6
