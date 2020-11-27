from __future__ import annotations
from typing import Any, Optional


class BstNode:
    def __init__(self, data: any, smaller: BstNode = None, bigger: BstNode = None):
        self.data = data
        self.smaller = smaller
        self.bigger = bigger

    # O(n) for the worst scenario when all nodes in the range (n is number of all nodes)
    # O(h) for the best scenario when no node in the range (h is height of the tree)
    def sum(self, min_val: int, max_val: int) -> Optional[int]:
        if min_val > max_val:
            return None
        res = 0
        if self.data > min_val and self.smaller:
            res += self.smaller.sum(min_val, max_val)
        if self.data < max_val and self.bigger:
            res += self.bigger.sum(min_val, max_val)
        if min_val <= self.data <= max_val:
            res += self.data
        return res


def build_tree(*args: Any, start: int = 0) -> Optional[BstNode]:
    if start >= len(args) or args[start] is None:
        return None
    new_node = BstNode(args[start])
    new_node.smaller = build_tree(*args, start=2 * start + 1)
    new_node.bigger = build_tree(*args, start=2 * start + 2)
    return new_node


assert build_tree(5, 3, 8, 2, 4, 6, 10).sum(4, 9) == 23
assert build_tree(10, 5, 50, 1, None, 40, 100).sum(5, 45) == 55

assert build_tree(10, 5, 50, 1, None, 40, 100).sum(101, 200) == 0
assert build_tree(10, 5, 50, 1, None, 40, 100).sum(-1, 0) == 0

assert build_tree(10, 5, 50, 1, None, 40, 100).sum(1, 0) is None
