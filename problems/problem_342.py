def reduce(arr, foo, default=None, init=None):
    try:
        elements = iter(arr)
        res = next(elements) if init is None else init
        for e in elements:
            res = foo(res, e)
        return res
    except StopIteration:
        return default


assert reduce([], lambda a, b: a + b) is None
assert reduce([], lambda a, b: a + b, default=200) == 200

assert reduce([100], lambda a, b: a + b) == 100
assert reduce([1, 2, 3], lambda a, b: a + b) == 6
assert reduce([2, 3, 4], lambda a, b: a * b) == 24
assert reduce([2, 3, 4], lambda a, b: a - b, init=100) == 91
