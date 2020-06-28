import collections


class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        parent = self.root
        while True:
            if parent.value == value:
                return
            if parent.value > value:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = new_node
                    return
            else:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = new_node
                    return

    def lookup(self, value):
        parent = self.root
        while parent:
            if parent.value == value:
                return parent
            if parent.value > value:
                parent = parent.left
            else:
                parent = parent.right
        return None


def test():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
