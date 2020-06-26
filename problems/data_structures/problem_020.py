from linked_list import LinkedList


def find_intersection(list_a, list_b):
    visited = [e.value for e in list_a]

    for element in list_b:
        if element.value in visited:
            return element.value
        element = element.next
    else:
        return None


linked_first = LinkedList().append(3).append(7).append(8).append(10)
linked_second = LinkedList().append(99).append(1).append(8).append(10)
print(find_intersection(linked_first, linked_second))