class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.length += 1

    def get_node(self, index):
        if index == 0:
            return self.head
        if index > self.length:
            return self.tail.next
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next
        return curr_node

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        if index >= self.length:
            self.append(data)
        else:
            new_node = Node(data)
            prev_node = self.get_node(index - 1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.previous = prev_node
            new_node.next = next_node
            self.length += 1

    def remove(self, index):
        node = self.get_node(index)
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node
        self.length -= 1


def test():
    double_list = DoublyLinkedList(1)
    double_list.append(3)
    double_list.prepend(0)
    double_list.insert(2, 2)
    double_list.remove(1)
    print()
