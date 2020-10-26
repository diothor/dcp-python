class Node:
    def __init__(self, value: any, next_node=None):
        self.data: any = value
        self.next: Node = next_node


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def _nodes_generator(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    # O(n)
    def append(self, value: any):
        if not self.head:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            else:
                last.next = Node(value)
        return self

    # O(n)
    def values(self):
        return [n.data for n in self._nodes_generator()]

    # O(n)
    def reverse(self):
        if self.head is None:
            raise ValueError('You want me to reverse None? Get lost!')
        _prev = None
        _curr = self.head
        while _curr:
            _next = _curr.next
            _curr.next = _prev
            _prev = _curr
            _curr = _next
        else:
            self.head = _prev
        return self


# few elements in order to reverse
list_to_test = LinkedList().append(1).append(2).append(3).append(4)
assert list_to_test.values() == [1, 2, 3, 4]
assert list_to_test.reverse().values() == [4, 3, 2, 1]

# single element in the list
assert LinkedList().append(100).reverse().values() == [100]

# empty list case
try:
    LinkedList().reverse()
    assert False
except ValueError:
    pass
