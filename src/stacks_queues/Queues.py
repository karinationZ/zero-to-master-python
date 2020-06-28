class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        second = self.first.next
        self.first.next = None
        self.first = second
        self.length -= 1


def test():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    print()


import collections


def test():
    q = collections.deque([1, 2, 3, 99])
    f_el = q.popleft()
    print(f_el)
    l_el = q.pop()
    print(l_el)
    q.append(100)
    q.appendleft(0)
    print(list(q))
