# find all cousins of given node in a binary tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = Node(left) if left else None
        self.right = Node(right) if right else None

    def left_val(self):
        return None if self.left is None else self.left.value

    def right_val(self):
        return None if self.right is None else self.right.value

    def parent_of(self, node: int):
        return node in [self.left_val(), self.right_val()]

    def __str__(self):
        return str(self.value)


def level(r: Node, value: int, lev=0) -> int:
    if r is None:
        return 0
    elif r.value == value:
        return lev + 1
    left_lev = level(r.left, value, lev + 1)
    if left_lev > 0:
        return left_lev
    return level(r.right, value, lev + 1)


def cousin_finder(r: Node, node: int, lev: int) -> list:
    if r is None:
        return []
    elif lev == 2 and r.parent_of(node):
        return []
    elif lev == 1:
        return [r.value]

    res = []
    res += cousin_finder(r.left, node, lev - 1)
    res += cousin_finder(r.right, node, lev - 1)
    return res


def cousins(r: Node, node: int) -> list:
    lev = level(r, node)
    return cousin_finder(r, node, lev)


root = Node(1, 2, 3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

assert level(root, 1) == 1
assert level(root, 2) == 2
assert level(root, 3) == 2
assert level(root, 4) == 3
assert level(root, 5) == 3
assert level(root, 6) == 3
assert level(root, 7) == 3
assert level(root, 10) == 0

c = cousins(root, 5)
assert c == [6, 7], c
