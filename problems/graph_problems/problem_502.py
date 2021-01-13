from typing import Optional


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'[{self.data} -> L: {self.left} R: {self.right}]'


def build(*args, index=0):
    if index >= len(args) or args[index] is None:
        return None
    root = Node(args[index])
    root.left = build(*args, index=2 * index + 1)
    root.right = build(*args, index=2 * index + 2)
    return root


# O(n)
def is_height_balanced(n: Optional[Node], h: int = 0) -> (bool, int):
    if n is None:
        return True, h
    lbalanced, lheight = is_height_balanced(n.left, h+1)
    rbalanced, rheight = is_height_balanced(n.right, h+1)
    return lbalanced and rbalanced and abs(lheight - rheight) < 2, max(lheight, rheight)


tree = build(0, 1, 2, None, 4, 5, 6)
assert is_height_balanced(tree) == (True, 3)

tree = build(0, None, 1, None, None, 2)
assert is_height_balanced(tree) == (False, 3)

assert is_height_balanced(None) == (True, 0)
assert is_height_balanced(Node(1)) == (True, 1)
