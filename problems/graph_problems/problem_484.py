from __future__ import annotations
from typing import Union, List, Any


class BstNode:
    def __init__(self, value: Any, smaller: BstNode = None, bigger: BstNode = None):
        self.data = value
        self.smaller = smaller
        self.bigger = bigger

    def __repr__(self) -> str:
        return f'data: {self.data}'

    # O(n)
    def is_valid(self) -> bool:
        valid = True
        if self.smaller:
            if self.smaller.data >= self.data:
                return False
            else:
                valid = self.smaller.is_valid()
        if self.bigger:
            if self.bigger.data <= self.data:
                return False
            else:
                valid &= self.bigger.is_valid()
        return valid

    # O(n)
    def in_order_reverersed(self) -> List[Any]:
        res = []
        if self.bigger:
            res += self.bigger.in_order_reverersed()
        res.append(self.data)
        if self.smaller:
            res += self.smaller.in_order_reverersed()
        return res

    # O(n)
    def second_largest(self) -> Any:
        data = self.in_order_reverersed()
        return data[1] if len(data) > 1 else None


def build_tree(*args: Any, start: int = 0) -> Union[BstNode, None]:
    if start >= len(args) or args[start] is None:
        return None
    new_node = BstNode(args[start])
    new_node.smaller = build_tree(*args, start=2 * start + 1)
    new_node.bigger = build_tree(*args, start=2 * start + 2)
    return new_node


munchkin_tree = build_tree(100)
assert munchkin_tree.is_valid() is True
assert munchkin_tree.second_largest() is None

tree = build_tree(2, 1)
assert tree.is_valid() is True
assert tree.second_largest() == 1

tree = build_tree(2, 1, 3, None, None, None, 4)
assert tree.in_order_reverersed() == [4, 3, 2, 1]
assert tree.is_valid() is True
assert tree.second_largest() == 3

tree = build_tree(2, 1, 5, None, None, 4)
assert tree.is_valid() is True
assert tree.second_largest() == 4

tree = build_tree(2, 1, 3)
assert tree.is_valid() is True
assert tree.second_largest() == 2

tree = build_tree(5, 2, None, 1, 3)
assert tree.is_valid() is True
assert tree.second_largest() == 3
