from __future__ import annotations

from collections import deque
from typing import Any, Optional


class BinaryTreeNode:

    def __init__(self, value: Any, left: BinaryTreeNode = None, right: BinaryTreeNode = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        res = f'value: {self.value}'
        if self.left:
            res += f' [left: {self.left}]'
        if self.right:
            res += f' [right: {self.right}]'
        return res


class BinaryTree:

    def __build_tree(*values, start: int = 0) -> Optional[BinaryTreeNode]:
        if start >= len(values) or values[start] is None:
            return None

        root = BinaryTreeNode(values[start])
        root.left = BinaryTree.__build_tree(*values, start=2 * start + 1)
        root.right = BinaryTree.__build_tree(*values, start=2 * start + 2)
        return root

    def __init__(self, *values):
        self.root = BinaryTree.__build_tree(*values)

    # O(n)
    def level_traversal(self):
        result = list()
        if not self.root:
            return result

        nodes = deque([self.root])
        while nodes:
            n = nodes.pop()
            result.append(n.value)
            if n.left:
                nodes.appendleft(n.left)
            if n.right:
                nodes.appendleft(n.right)
        else:
            return result


assert BinaryTree(1, 2, 3, None, None, 4, 5).level_traversal() == [1, 2, 3, 4, 5]
assert BinaryTree(None).level_traversal() == []
assert BinaryTree(20, 8, 22, 4, 12, None, None, None, None, 10, 14).level_traversal() == [20, 8, 22, 4, 12, 10, 14]
