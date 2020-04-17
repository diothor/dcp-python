def trees(end: int, start: int = 0) -> list:
    if start >= end:
        return [None]

    roots = []
    for value in range(start, end):
        on_left = trees(start=start, end=value)
        on_right = trees(start=value + 1, end=end)

        for lefty in on_left:
            for righty in on_right:
                node = Node(value, lefty, righty)
                roots.append(node)
    return roots


def preorder(node):
    result = [node.value]
    if node.left:
        result += preorder(node.left)
    if node.right:
        result += preorder(node.right)
    return result


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
