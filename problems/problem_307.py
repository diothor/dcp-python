class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'v:{self.value}'


def make_tree(nodes: list, root_node=0) -> Node or None:
    if root_node >= len(nodes):
        return None
    root = Node(nodes[root_node])
    root.left = make_tree(nodes, 2 * root_node + 1)
    root.right = make_tree(nodes, 2 * root_node + 2)
    return root


def __floor(value: int, node: Node) -> Node or None:
    if node is None:
        return None
    elif node.value == value:
        return node
    elif node.value > value:
        return __floor(value, node.left)
    elif node.value < value:
        res = __floor(value, node.right)
        return res if res else node


def __ceil(value: int, node: Node) -> Node or None:
    if node is None:
        return None
    elif node.value == value:
        return node
    elif node.value < value:
        return __ceil(value, node.right)
    elif node.value > value:
        res = __ceil(value, node.left)
        return res if res else node


def floor_ceil(value: int, node: Node) -> list:
    floor_value = __floor(value, node)
    if floor_value:
        floor_value = floor_value.value
    ceil_value = __ceil(value, node)
    if ceil_value:
        ceil_value = ceil_value.value
    return [floor_value, ceil_value]


test_bst = make_tree([8, 4, 10, 2, 6, 9, 12])
assert floor_ceil(3, test_bst) == [2, 4]
assert floor_ceil(5, test_bst) == [4, 6]
assert floor_ceil(1, test_bst) == [None, 2]
assert floor_ceil(9, test_bst) == [9, 9]
assert floor_ceil(7, test_bst) == [6, 8]
