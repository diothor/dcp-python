from __future__ import annotations
from typing import Optional, Dict, List


class BinaryTreeNode:
    def __init__(self, value, left: BinaryTreeNode = None, right: BinaryTreeNode = None):
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


def build_tree(*values, start: int = 0) -> Optional[BinaryTreeNode]:
    if start >= len(values) or values[start] is None:
        return None

    root = BinaryTreeNode(values[start])
    root.left = build_tree(*values, start=2 * start + 1)
    root.right = build_tree(*values, start=2 * start + 2)
    return root


def tree_subsums(root: BinaryTreeNode, sums: Dict[int, int] = None) -> int:
    if root is None:
        return 0
    elif sums is None:
        sums = {}
    this_sum = root.value + tree_subsums(root.left, sums) + tree_subsums(root.right, sums)
    sums[this_sum] = sums.setdefault(this_sum, 0) + 1
    return this_sum


# O(n) where n is number of nodes in the tree
def most_frequent_subsums(tree: Optional[BinaryTreeNode]) -> List[int]:
    subsums = {}
    tree_subsums(tree, subsums)
    max_freq = max(subsums.values(), default=0)
    return list(sorted([ssum for ssum, freq in subsums.items() if freq == max_freq]))


# basic test cases
assert most_frequent_subsums(None) == []
assert most_frequent_subsums(build_tree(7)) == [7]
assert most_frequent_subsums(build_tree(2, 17, -1, None, None, 0, -1)) == [17]
assert most_frequent_subsums(build_tree(1, 3, 2)) == [2, 3, 6]

# acceptance test from the task
test_tree = build_tree(5, 2, -5)
assert most_frequent_subsums(test_tree) == [2]
