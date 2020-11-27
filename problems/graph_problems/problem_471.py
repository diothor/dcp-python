from __future__ import annotations
from typing import Optional, List


class BstNode:
    def __init__(self, value: any, smaller: BstNode = None, bigger: BstNode = None):
        self.data = value
        self.smaller = smaller
        self.bigger = bigger

    def pre_order(self) -> List[any]:
        order = [self.data]
        if self.smaller:
            order += self.smaller.pre_order()
        if self.bigger:
            order += self.bigger.pre_order()
        return order


def build_tree(*args, start: int = 0) -> Optional[BstNode]:
    if start >= len(args) or args[start] is None:
        return None
    root = BstNode(args[start])
    root.smaller = build_tree(*args, start=2 * start + 1)
    root.bigger = build_tree(*args, start=2 * start + 2)
    return root


def print_tree(tree_to_print: BstNode, padding: str = '', prefix: str = '', level: int = 0) -> None:
    if not tree_to_print:
        return
    print(padding + prefix + str(tree_to_print.data))

    right_padding = '' if level < 1 else padding + '|   '
    print_tree(tree_to_print.smaller, right_padding, '├── ' if tree_to_print.bigger else '└── ', level + 1)

    left_padding = '' if level < 1 else padding + '    '
    print_tree(tree_to_print.bigger, left_padding, '└── ', level + 1)


tree = build_tree(1, 2, 3, 4, 5, 6, None, 7, 8, 9, 10, 11, 12)
print_tree(tree)
