from __future__ import annotations
from typing import Optional, Any
from operator import itemgetter


class BinaryTree:
    def __init__(self, data):
        self.data: Any = data
        self.left: Optional[BinaryTree] = None
        self.right: Optional[BinaryTree] = None

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other

    def in_order(self, res=None) -> list:
        if res is None:
            res = []
        if self.left:
            self.left.in_order(res)
        res.append(self.data)
        if self.right:
            self.right.in_order(res)
        return res


def build(*args, size: int = -1, index: int = 0) -> Optional[BinaryTree]:
    if size < 0:
        size = len(args)
    if index >= size or args[index] is None:
        return None
    else:
        node = BinaryTree(args[index])
        node.left = build(*args, size=size, index=2 * index + 1)
        node.right = build(*args, size=size, index=2 * index + 2)
        return node


# O(n) where n is number of nodes in the tree
def deepest(tree: BinaryTree, level: int = 1) -> (Any, int):
    if tree.left is None and tree.right is None:
        return tree, level
    deep_left = (None, -1) if tree.left is None else deepest(tree.left, level + 1)
    deep_right = (None, -1) if tree.right is None else deepest(tree.right, level + 1)
    return max(deep_right, deep_left, key=itemgetter(1))


assert deepest(build('a', 'b', 'c', 'd')) == ('d', 3)
assert deepest(build('a', 'b', 'c')) == ('c', 2)

assert deepest(build(100)) == (100, 1)
assert deepest(build(1, 2, 3, 4, 5, 6, 7)) == (7, 3)

assert deepest(build(1, 2, 3, 4, 5, 6, 7, 8)) == (8, 4)
assert deepest(build(1, 2, 3, None, None, 6)) == (6, 3)
