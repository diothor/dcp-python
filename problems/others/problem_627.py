class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self._peeked = None

    def peek(self):
        return self._peeked if self.has_next() else None

    def next(self):
        res = next(self.iterator) if self._peeked is None else self._peeked
        self._peeked = None
        return res

    def has_next(self):
        if self._peeked is not None:
            return True
        try:
            self._peeked = next(self.iterator)
            return True
        except StopIteration:
            return False


peekable = PeekableInterface(iter([]))
assert peekable.has_next() is False

peekable = PeekableInterface(iter([1]))
assert peekable.has_next() is True
assert peekable.peek() == 1
assert peekable.has_next() is True
assert peekable.next() == 1
assert peekable.has_next() is False

peekable = PeekableInterface(iter([1, 2, 3, 4]))
assert peekable.next() == 1
assert peekable.peek() == 2
assert peekable.has_next() is True
assert peekable.next() == 2
assert peekable.next() == 3
assert peekable.peek() == 4
assert peekable.next() == 4
assert peekable.peek() is None
assert peekable.has_next() is False
try:
    peekable.next()
    assert False
except StopIteration:
    pass
