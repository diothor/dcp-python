from typing import Optional, Any


class SparseArray:

    def __init__(self):
        self.storage = {}
        self.size = 0

    def __repr__(self):
        return f'values: {self.storage}, size: {self.size}'

    def values(self):
        return self.storage.copy()

    def init(self, arr: list, size):
        if size < len(arr):
            raise ValueError
        self.size = size
        self.storage = {}
        for i, v in enumerate(arr):
            if v != 0:
                self.storage[i] = v

    def set(self, i: int, val: Optional[Any]):
        if i >= self.size:
            raise IndexError
        if val != 0:
            self.storage[i] = val
        else:
            del self.storage[i]

    def get(self, i: int) -> Optional[Any]:
        if i >= self.size:
            raise IndexError
        return self.storage.get(i) if i in self.storage else 0


# test init(arr, size)
array = SparseArray()
array.init([1, None, 2, 0, 0, 0, 0, 0, 1], 100)
assert array.size == 100
assert array.storage.keys() == {0, 1, 2, 8}

array.init([0, 0, 1], 7)
assert array.size == 7
assert array.storage.keys() == {2}

try:
    array.init([1, 1], 1)
    assert False
except ValueError:
    pass

# test set(i, v)
array = SparseArray()
try:
    array.set(0, 1)
    assert False
except IndexError:
    pass

array.init([], 20)
assert array.storage.keys() == set()
assert array.size == 20

array.set(3, 1)
assert array.storage.keys() == {3}
array.set(7, 1)
assert array.storage.keys() == {3, 7}
array.set(19, 1)
assert array.storage.keys() == {3, 7, 19}
array.set(7, 0)
assert array.storage.keys() == {3, 19}
array.set(19, 1)
assert array.storage == {3: 1, 19: 1}
array.set(19, '1')
assert array.storage == {3: 1, 19: '1'}
array.set(15, None)
assert array.storage == {3: 1, 19: '1', 15: None}

# test get(i)
array = SparseArray()
array.init([0, '1', 0, 1, 2], 10)
assert array.get(0) == 0
assert array.get(1) == '1'
assert array.get(3) == 1
assert array.get(4) == 2
assert array.get(9) == 0
try:
    array.get(10)
    assert False
except IndexError:
    pass
