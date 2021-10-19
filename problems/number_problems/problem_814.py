from __future__ import annotations
from typing import Optional


class LinkedListNode:
    def __init__(self, value, next_node: LinkedListNode = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ('' if self.next is None else str(self.next))


def num2list(number: int) -> LinkedListNode:
    number, digit = divmod(number, 10)
    root = current = LinkedListNode(digit)
    while number > 0:
        number, digit = divmod(number, 10)
        current.next = LinkedListNode(digit)
        current = current.next
    else:
        return root


assert str(num2list(1234)) == '4321'
assert str(num2list(100)) == '001'
assert str(num2list(0)) == '0'


# O(n) where n is the length of a longer list
def sum_linked_lists(list_a: LinkedListNode, list_b: LinkedListNode, extra_one: int = 0) -> Optional[LinkedListNode]:
    sum_value = extra_one
    if list_a is not None:
        sum_value += list_a.value
        list_a = list_a.next
    if list_b is not None:
        sum_value += list_b.value
        list_b = list_b.next

    if sum_value > 0:
        new_extra_one, digit = divmod(sum_value, 10)
        return LinkedListNode(digit, sum_linked_lists(list_a, list_b, new_extra_one))
    else:
        return None


assert str(sum_linked_lists(num2list(99), num2list(25))) == '421'
assert str(sum_linked_lists(num2list(999), num2list(1))) == '0001'
