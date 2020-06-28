# Create a Linked List with:
# append/prepend/insert methods
#


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        if index >= self.length:
            self.append(data)
        new_node = Node(data)
        prev_node = self.get_node(index - 1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node
        self.length += 1

    def get_node(self, index):
        if index > self.length:
            return self.tail.next
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next

        return curr_node

    def remove(self, index):
        prev_node = self.get_node(index - 1)
        next_node = prev_node.next.next
        prev_node.next = next_node
        self.length -= 1

    def reverse(self):
        if self.length == 1:
            return
        prev_node = self.head
        curr_node = prev_node.next
        prev_node.next = self.tail.next
        self.tail = self.head
        while curr_node.next:
            temp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_node

        self.head = curr_node
        curr_node.next = prev_node

    def print_list(self):
        lst = [self.head.value]
        node = self.head
        while node.next:
            node = node.next
            lst.append(node.value)
        print(lst)


def test():
    l = LinkedList(1)
    l.prepend(10)
    l.print_list()
    l.reverse()
    l.print_list()
