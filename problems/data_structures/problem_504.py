class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.next = 0
        self.buffer = [None]*size

    def __str__(self):
        return str(self.buffer)

    # O(1)
    def record(self, order_id: any):
        self.buffer[self.next] = order_id
        self.next = (self.next + 1) % self.size
        return self

    # O(1)
    def get_last(self, ith: int) -> any:
        if ith >= self.size:
            raise ValueError()
        ith = self.next - ith - 1
        if ith < 0:
            ith += self.size
        return self.buffer[ith]


log = CircularBuffer(3)
log.record(1).record(2)
assert log.buffer == [1, 2, None]
assert log.get_last(0) == 2
assert log.get_last(1) == 1
assert log.get_last(2) is None
try:
    log.get_last(3)
    assert False
except ValueError:
    pass

log.record(3)
assert log.buffer == [1, 2, 3]
assert log.get_last(0) == 3
assert log.get_last(2) == 1
try:
    log.get_last(3)
    assert False
except ValueError:
    pass

log.record(4)
assert log.buffer == [4, 2, 3]
assert log.get_last(0) == 4
assert log.get_last(2) == 2
try:
    log.get_last(3)
    assert False
except ValueError:
    pass

log.record(5)
assert log.buffer == [4, 5, 3]
