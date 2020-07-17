from typing import Union
import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'(v: {self.value}, l: {self.left}, r: {self.right})'


def calculate(node: Node) -> Union[int, float, None]:
    if node.left is None and node.right is None:
        return node.value

    left = calculate(node.left)
    right = calculate(node.right)
    return ops.get(node.value)(left, right) if node.value in ops else None


def flatarr2tree(arr: list, node_index: int = 0) -> Union[Node, None]:
    if node_index >= len(arr):
        return None
    node_obj = Node(arr[node_index])
    node_obj.left = flatarr2tree(arr, 2 * node_index + 1)
    node_obj.right = flatarr2tree(arr, 2 * node_index + 2)
    return node_obj if node_obj.value else None


assert calculate(Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))) == 45
assert calculate(flatarr2tree(['*', '+', '+', 3, '-', 4, 5, None, None, 7, 2])) == 72
