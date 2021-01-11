from __future__ import annotations


class MyLinkedList:
    def __init__(self, data, next_node: MyLinkedList = None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data) + (f' -> {str(self.next)}' if self.next else '')


def build(*args) -> MyLinkedList:
    current = root = MyLinkedList(args[0])
    for val in args[1:]:
        current.next = MyLinkedList(val)
        current = current.next
    return root


# O(n)
def remove__kth(root: MyLinkedList, k: int) -> MyLinkedList:
    start = root
    kth = root
    while k > 0:
        if kth is None:
            raise ValueError('k is bigger than list size')
        kth = kth.next
        k -= 1
    if kth is None:
        return root.next
    while kth.next:
        start = start.next
        kth = kth.next
    start.next = start.next.next
    return root


linked_list = build(1, 2, 3, 4, 5)
assert str(remove__kth(linked_list, 2)) == '1 -> 2 -> 3 -> 5'

linked_list = build(1, 2, 3, 4, 5)
assert str(remove__kth(linked_list, 1)) == '1 -> 2 -> 3 -> 4'

linked_list = build(1, 2, 3, 4, 5)
assert str(remove__kth(linked_list, 5)) == '2 -> 3 -> 4 -> 5'

linked_list = build(1, 2, 3, 4, 5)
try:
    remove__kth(linked_list, 6)
    assert False
except ValueError:
    pass
