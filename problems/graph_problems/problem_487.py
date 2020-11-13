from __future__ import annotations
from typing import Union, List, Tuple, Any


class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Union[BinaryNode, None] = None
        self.right: Union[BinaryNode, None] = None

    def __repr__(self):
        return f'val: {self.value}'

    # O(n)
    def pre_order(self) -> List[Any]:
        values = [self.value]
        if self.left:
            values += self.left.pre_order()
        if self.right:
            values += self.right.pre_order()
        return values

    # O(n)
    def level(self, node_valu: Any, current: int = 1) -> Union[int, None]:
        if self.value == node_valu:
            return current
        res = None
        if self.left:
            res = self.left.level(node_valu, current + 1)
        if not res and self.right:
            res = self.right.level(node_valu, current + 1)
        return res

    def find_parent(self, node_val) -> Tuple[Union[BinaryNode, None], Union[bool, None]]:
        if self.left and self.left.value == node_val:
            return self, True
        if self.right and self.right.value == node_val:
            return self, False
        res = None
        left_side = None
        if self.left:
            res, left_side = self.left.find_parent(node_val)
        if not res and self.right:
            res, left_side = self.right.find_parent(node_val)
        return res, left_side

    def find_sibling(self, node_val: Any) -> Union[Any, None]:
        (parent, left_side) = self.find_parent(node_val)
        if not parent:
            return None
        elif left_side:
            return parent.right.value if parent.right else None
        else:
            return parent.left.value if parent.left else None

    def all_from_level(self, level, nodes=None) -> List[BinaryNode]:
        if nodes is None:
            nodes = []
        if level == 1:
            nodes.append(self.value)
            return nodes
        if self.left:
            self.left.all_from_level(level - 1, nodes)
        if self.right:
            self.right.all_from_level(level - 1, nodes)
        return nodes

    def cousins(self, node_value: Any) -> List[Any]:
        level = self.level(node_value)
        if level is None:
            return list()
        values_on_level = self.all_from_level(level)
        values_on_level.remove(node_value)
        sibling_value = self.find_sibling(node_value)
        if sibling_value is not None:
            values_on_level.remove(sibling_value)
        return values_on_level


def build_tree(*args, index=0) -> Union[BinaryNode, None]:
    if index >= len(args) or args[index] is None:
        return None
    node = BinaryNode(args[index])
    node.left = build_tree(*args, index=2 * index + 1)
    node.right = build_tree(*args, index=2 * index + 2)
    return node


# build tree to test
test_tree = build_tree(1, 2, 3, 4, 5, 6)

# check if BinaryNode:level() works
assert test_tree.level(1) == 1
assert test_tree.level(5) == 3
assert test_tree.level(-1) is None

# check if BinaryNode:sibling() works
assert test_tree.find_sibling(1) is None
assert test_tree.find_sibling(2) == 3
assert test_tree.find_sibling(3) == 2
assert test_tree.find_sibling(5) == 4

# check if BinaryNode:all_from_level() works
assert test_tree.all_from_level(1) == [1]
assert test_tree.all_from_level(2) == [2, 3]
assert test_tree.all_from_level(3) == [4, 5, 6]

# test example from the task
assert test_tree.cousins(5) == [6]
# test if value not in the tree
assert test_tree.cousins(10) == []
# test when value does not have any cousins, but has a simbling
assert test_tree.cousins(2) == []
# test if value in the root (has neither cousins nor simblings)
assert test_tree.cousins(1) == []

# test when value does not have any simbling
test_tree = build_tree(1, 2, 3, 4, None, 6)
assert test_tree.cousins(4) == [6]

# test another tree
another_tree = build_tree(6, 13, 5, 7, 8, 1, 3)
assert another_tree.cousins(7) == [1, 3]
assert another_tree.cousins(8) == [1, 3]
assert another_tree.cousins(1) == [7, 8]
assert another_tree.cousins(3) == [7, 8]

# when duplicates are present, always higher node is taken - could be improved, too lasy to change find_parent() method :)
with_duplicates = build_tree(1, 2, 3, 4, 5, 6, 2)
assert with_duplicates.cousins(2) == []
assert with_duplicates.cousins(4) == [6, 2]
