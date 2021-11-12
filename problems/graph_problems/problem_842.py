from __future__ import annotations
from typing import Any, Optional


class BinaryTree:
    def __init__(self, value: Any, left: BinaryTree = None, right: BinaryTree = None):
        self.value: Any = value
        self.left: BinaryTree = left
        self.right: BinaryTree = right

    def __repr__(self):
        return str(self.value)

    def in_order(self, res=None) -> list:
        if res is None:
            res = []
        if self.left:
            self.left.in_order(res)
        res.append(self.value)
        if self.right:
            self.right.in_order(res)
        return res

    def invert(self) -> BinaryTree:
        if self.left is not None:
            self.left.invert()
        if self.right is not None:
            self.right.invert()
        self.left, self.right = self.right, self.left
        return self


def build(*args: Any, size: int = -1, index: int = 0) -> Optional[BinaryTree]:
    if size < 0:
        size = len(args)
    if index >= size or args[index] is None:
        return None
    node = BinaryTree(args[index])
    node.left = build(*args, size=size, index=2 * index + 1)
    node.right = build(*args, size=size, index=2 * index + 2)
    return node


assert build('a', 'b', 'c').invert().in_order() == ['c', 'a', 'b']
assert build('a', None, 'c').invert().in_order() == ['c', 'a']
assert build('a', 'b', None).invert().in_order() == ['a', 'b']

# Acceptance case
test_tree = build('a', 'b', 'c', 'd', 'e', 'f')
assert test_tree.in_order() == ['d', 'b', 'e', 'a', 'f', 'c']
assert test_tree.invert().in_order() == ['c', 'f', 'a', 'e', 'b', 'd']
