from typing import Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Node = left
        self.right: Node = right

    def in_order(self) -> list:
        res = self.left.in_order() if self.left else []
        res.append(self.value)
        res += self.right.in_order() if self.right else []
        return res

    def __str__(self):
        return f'[value: {self.value} left: {self.left} right: {self.right}]'


def build_tree(*args, start: int = 0) -> Optional[Node]:
    if start >= len(args) or args[start] is None:
        return None
    root = Node(args[start])
    root.left = build_tree(*args, start=2 * start + 1)
    root.right = build_tree(*args, start=2 * start + 2)
    return root


def min_sum(root) -> (int, list):
    msum, mpath = min_sum_helper(root)
    mpath.reverse()
    return msum, mpath


# O(n)
def min_sum_helper(root: Node) -> (int, list):
    if root is None:
        return 0, []

    sum_left, path_left = min_sum_helper(root.left)
    sum_right, path_right = min_sum_helper(root.right)

    if root.right is not None and (root.left is None or sum_right <= sum_left):
        path_right.append(root.value)
        return root.value + sum_right, path_right
    else:
        path_left.append(root.value)
        return root.value + sum_left, path_left


test_root = build_tree(1, None, 2)
assert min_sum(test_root) == (3, [1, 2])

test_root = build_tree(1, 2, None)
assert min_sum(test_root) == (3, [1, 2])

test_root = build_tree(10, 5, 5, None, 2, None, 1, None, None, None, None, None, None, -1, None)
assert test_root.in_order() == [5, 2, 10, 5, -1, 1]
assert min_sum(test_root) == (15, [10, 5, 1, -1])

test_root = build_tree(10, -2, 7, 8, -4)
assert test_root.in_order() == [8, -2, -4, 10, 7]
assert min_sum(test_root) == (4, [10, -2, -4])

test_root = build_tree(1, 2, 3, 8, 4, 5, 6, None, None, 10, None, 7, 9, None, 5)
assert test_root.in_order() == [8, 2, 10, 4, 1, 7, 5, 9, 3, 6, 5]
assert min_sum(test_root) == (11, [1, 2, 8])
