from __future__ import annotations


class LinkedListNode:
    def __init__(self, value, next_node: LinkedListNode = None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f'{str(self.value)} -> {str(self.next)}' if self.next else str(self.value)

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            res = self.current.value
            self.current = self.current.next
            return res


# O(n)
def build_linked_list(*values) -> LinkedListNode:
    if not values:
        return LinkedListNode(None)

    head = LinkedListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = LinkedListNode(v)
        current = current.next
    else:
        return head


# O(n)
def swap_every_two(linked_list: LinkedListNode):
    first = linked_list
    if not first or not first.next:
        return first

    second = first.next
    third = swap_every_two(second.next) if second.next else None

    first.next, second.next = third, first
    return second


assert list(swap_every_two(build_linked_list(1, 2, 3, 4))) == [2, 1, 4, 3]
assert list(swap_every_two(build_linked_list(1, 2, 3, 4, 5))) == [2, 1, 4, 3, 5]
