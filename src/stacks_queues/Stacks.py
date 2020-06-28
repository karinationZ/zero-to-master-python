class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None


class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            self.top.next = new_node
            new_node.previous = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return
        else:
            second_last = self.top.previous
            self.top = second_last
            second_last.next = None
            self.length -= 1


class Stack2:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def push(self, data):
        self.stack.append(data)
        return

    def pop(self):
        if not self.stack:
            return None
        else:
            self.stack.pop()
        return self.stack
