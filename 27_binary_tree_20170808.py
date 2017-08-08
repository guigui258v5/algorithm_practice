class Node(object):
    """节点"""
    def __init__(self, elem, llink=None, rlink=None):
        self.elem = elem
        self.llink = llink
        self.rlink = rlink


class Tree(object):
    """二叉树"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """添加节点"""
        node = Node(elem)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            ref = queue.pop(0)
            if ref.llink is None:
                ref.llink = node
                return
            else:
                queue.append(ref.llink)

            if ref.rlink is None:
                ref.rlink = node
                return
            else:
                queue.append(ref.rlink)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            print('empty')
            return
        queue = [self.root]
        while queue:
            ref = queue.pop(0)
            print(ref.elem, end = ' ')
            if ref.llink is not None:
                queue.append(ref.llink)
            if ref.rlink is not None:
                queue.append(ref.rlink)

    def preorder_travel(self, node):
        if node is None:
            return
        print(node.elem, end = ' ')
        self.preorder_travel(node.llink)
        self.preorder_travel(node.rlink)

    def inorder_travel(self, node):
        if node is None:
            return
        self.inorder_travel(node.llink)
        print(node.elem, end = ' ')
        self.inorder_travel(node.rlink)

    def postorder_travel(self, node):
        if node is None:
            return
        self.postorder_travel(node.llink)
        self.postorder_travel(node.rlink)
        print(node.elem, end = ' ')

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()
    print('')
    tree.preorder_travel(tree.root)
    print('')
    tree.inorder_travel(tree.root)
    print('')
    tree.postorder_travel(tree.root)
