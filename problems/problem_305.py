class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f'v:{self.value}'

    def __iter__(self):
        self.head = self
        return self

    def __next__(self):
        if self.head:
            head_copy, self.head = self.head, self.head.next
            return head_copy
        else:
            raise StopIteration

    def as_array(self):
        return [i.value for i in self]

    @staticmethod
    def from_array(arr: list):
        res = head = ListNode(arr[0])
        for v in arr[1:]:
            head.next = head = ListNode(v)
        return res


def rm_zero_sum_sublist(linked_list: ListNode) -> list:
    very_first = ListNode(None, linked_list)
    acc_sums = {0: very_first}
    accumulator = 0
    
    for node in linked_list:
        accumulator += node.value
        if accumulator in acc_sums:
            node_to_rem = acc_sums[accumulator].next
            acc_to_rem = accumulator + node_to_rem.value
            while node_to_rem != node:
                del(acc_sums[acc_to_rem])
                node_to_rem = node_to_rem.next
                acc_to_rem += node_to_rem.value
            else:
                acc_sums[accumulator].next = node.next
        else:
            acc_sums[accumulator] = node

    return very_first.next.as_array()


assert rm_zero_sum_sublist(ListNode.from_array([3, 4, -7, 5, -6, 6])) == [5]
