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

    def breadth_first_search(self):
        curr_node = self.root
        q = collections.deque([curr_node])
        lst = []
        while q:
            curr_node = q.popleft()
            lst.append(curr_node.value)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        return lst

    def breadth_first_search_rec(self, queue, lst):
        if not queue:
            return lst
        else:
            curr_node = queue.popleft()
            lst.append(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            return self.breadth_first_search_rec(queue, lst)

    def dfs_in_order(self):
        return traverse_in_order(self.root, [])

    def dfs_pre_order(self):
        return traverse_pre_order(self.root, [])

    def dfs_post_order(self):
        return traverse_post_order(self.root, [])


def traverse_in_order(node, lst):
    if node.left:
        traverse_in_order(node.left, lst)
    lst.append(node.value)
    if node.right:
        traverse_in_order(node.right, lst)
    return lst


def traverse_pre_order(node, lst):
    lst.append(node.value)
    if node.left:
        traverse_pre_order(node.left, lst)
    if node.right:
        traverse_pre_order(node.right, lst)
    return lst


def traverse_post_order(node, lst):
    if node.left:
        traverse_post_order(node.left, lst)
    if node.right:
        traverse_post_order(node.right, lst)
    lst.append(node.value)

    return lst


# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

def check_bst(node, min_val, max_val):
    if not node:
        return True
    if node.val <= min_val or node.val >= max_val:
        return False
    valid_left = check_bst(node.left, min_val, node.val)
    valid_right = check_bst(node.right, node.val, max_val)
    return valid_left and valid_right


def check_valid_bst(root):
    if not root:
        return True
    return check_bst(root, float("-inf"), float("inf"))
