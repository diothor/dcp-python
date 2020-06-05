class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def inorder(node: Node, result: list = None) -> list:
    if result is None:
        result = []
    if node is None:
        return result
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)
    return result


def create(*args, node: Node = None, index: int = 0):
    if node is None and index < len(args):
        node = Node(args[index])

    try:
        node.left = None if args[2 * index + 1] is None else Node(args[2 * index + 1])
        node.right = None if args[2 * index + 2] is None else Node(args[2 * index + 2])
    except IndexError:
        return node

    create(*args, node=node.left, index=index + 1)
    create(*args, node=node.right, index=index + 2)
    return node


def merge(tree_a: Node, tree_b: Node):
    if tree_a is None and tree_b is None:
        return None
    merged = Node((0 if tree_a is None else tree_a.value) + (0 if tree_b is None else tree_b.value))
    merged.left = merge(None if tree_a is None else tree_a.left, None if tree_b is None else tree_b.left)
    merged.right = merge(None if tree_a is None else tree_a.right, None if tree_b is None else tree_b.right)
    return merged


first = create(2, 1, 4, 5)
assert inorder(first) == [5, 1, 2, 4]

second = create(3, 6, 1, None, 2, None, 7)
assert inorder(second) == [6, 2, 3, 1, 7]

node_sum = merge(first, second)
assert inorder(node_sum) == [5, 7, 2, 5, 5, 7]
