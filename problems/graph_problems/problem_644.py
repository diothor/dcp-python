from typing import Any, Optional
from operator import add


class BinaryNode:
    def __init__(self, value):
        self.left: Optional[BinaryNode] = None
        self.right: Optional[BinaryNode] = None
        self.data = value

    def children_data(self):
        res = []
        if self.left:
            res.append(self.left.data)
        if self.right:
            res.append(self.right.data)
        return res

    def __repr__(self):
        return str(self.data)


def build_tree(*args: Any, size: int = -1, start: int = 0) -> Optional[BinaryNode]:
    if size < 0:
        size = len(args)
    if start >= size or args[start] is None:
        return None

    root = BinaryNode(args[start])
    root.left = build_tree(*args, size=size, start=2 * start + 1)
    root.right = build_tree(*args, size=size, start=2 * start + 2)
    return root


# O(n)
def unival_vs_all_subtrees(root: BinaryNode) -> (int, int):
    if root is None:
        return 0, 0
    all_unival_num, all_subtree_num = map(add, unival_vs_all_subtrees(root.left), unival_vs_all_subtrees(root.right))
    is_unival = all_unival_num == all_subtree_num and all(v == root.data for v in root.children_data())
    return all_unival_num + is_unival, all_subtree_num + 1


# Basic positive cases
assert unival_vs_all_subtrees(build_tree('A')) == (1, 1)
assert unival_vs_all_subtrees(build_tree('A', 'A')) == (2, 2)
assert unival_vs_all_subtrees(build_tree('A', None, 'A')) == (2, 2)
assert unival_vs_all_subtrees(build_tree('A', 'A', 'A')) == (3, 3)

# Basic negative cases
assert unival_vs_all_subtrees(build_tree('A', 'B')) == (1, 2)
assert unival_vs_all_subtrees(build_tree('A', None, 'B')) == (1, 2)
assert unival_vs_all_subtrees(build_tree('A', 'B', 'A')) == (2, 3)
assert unival_vs_all_subtrees(build_tree('A', 'A', 'B')) == (2, 3)

# Nonadjacent values
assert unival_vs_all_subtrees(build_tree('B', 'B', 'B', 'A', None, None, None, 'A', 'A')) == (4, 6)

# Acceptance cases
assert unival_vs_all_subtrees(build_tree(0, 1, 0, None, None, 1, 0, None, None, None, None, 1, 1)) == (5, 7)
assert unival_vs_all_subtrees(build_tree(5, 1, 5, 5, 5, None, 5)) == (4, 6)
assert unival_vs_all_subtrees(build_tree(5, 4, 5, 4, 4, None, 5)) == (5, 6)
