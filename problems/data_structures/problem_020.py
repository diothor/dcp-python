from linked_list import LinkedList


# O(n + m)
def find_intersection(list_a, list_b):
    visited = {hash(e.value) for e in list_a}  # O(n)

    for element in list_b:  # O(m)
        if hash(element.value) in visited:
            return element.value
        element = element.next
    else:
        return None


linked_first = LinkedList().append(3).append(7).append(8).append(10)
linked_second = LinkedList().append(99).append(1).append(8).append(10)
assert find_intersection(linked_first, linked_second) == 8
