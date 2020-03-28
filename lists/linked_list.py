class LinkedListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        self.head = LinkedListNode(new_value, self.head)

    def append(self, new_value):
        new_node = LinkedListNode(value=new_value)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        return self

    def __str__(self):
        out = []
        current = self.head
        while current:
            out.append(current.value)
            current = current.next
        return str(out)

    def __iter__(self):
        self.cursor = self.head
        return self

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        output, self.cursor= self.cursor, self.cursor.next
        return output
