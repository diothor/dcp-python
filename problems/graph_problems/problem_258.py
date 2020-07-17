import math


class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def walk(tree: Node) -> list:
    traversal = []
    next_level = []
    current_level = [tree]

    left_to_right = True
    while current_level:
        node = current_level.pop()
        traversal.append(node.root)

        if left_to_right:
            children = [node.left, node.right]
        else:
            children = [node.right, node.left]
        next_level += filter(lambda x: x is not None, children)

        if not current_level:
            current_level, next_level = next_level, []
            left_to_right = not left_to_right

    return traversal


input_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(walk(input_tree))
input_tree = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10), Node(11))), Node(3, Node(6), Node(7, Node(12), Node(13))))
print(walk(input_tree))