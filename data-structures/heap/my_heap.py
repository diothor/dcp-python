from operator import itemgetter


class Heap:

    def __init__(self, *storage):
        self.storage = list(storage)
        for i in range(len(storage) // 2, -1, -1):
            self.__heapify_children(i)

    def __node(self, index):
        if index < len(self.storage):
            return {'index': index, 'value': self.storage[index]}
        else:
            return None

    def __parent(self, child):
        if child < 1:
            return None
        parent = (child - 1) // 2
        return self.__node(parent)

    def __left(self, parent: int):
        left = 2 * parent + 1
        return self.__node(left)

    def __right(self, parent):
        right = 2 * parent + 2
        return self.__node(right)

    def __swap(self, a: int, b: int):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]

    def __heapify_children(self, index):
        children = filter(lambda ch: ch is not None, [self.__left(index), self.__right(index)])
        small_child = min(children, key=itemgetter('value', 'index'), default=None)

        if small_child and small_child['value'] < self.storage[index]:
            self.storage[index], self.storage[small_child['index']] = self.storage[small_child['index']], self.storage[index]
            self.__heapify_children(small_child['index'])

    def __heapify_parents(self, index):
        parent = self.__parent(index)
        if parent and parent['value'] > self.storage[index]:
            self.__swap(index, parent['index'])
            self.__heapify_parents(parent['index'])

    def push(self, value):
        index = len(self.storage)
        self.storage.append(value)
        self.__heapify_parents(index)
        return self

    def pop(self):
        head = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage = self.storage[:-1]
        self.__heapify_children(0)
        return head

    def __str__(self):
        return str(self.storage)
