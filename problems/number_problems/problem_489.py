# O(n)
def size_distinct(arr: list) -> int:
    max_size = start = 0
    vals = {}
    for i, v in enumerate(arr):
        if v in vals and vals[v] >= start:
            max_size = max(max_size, i - start)
            start = vals[v] + 1
        vals[v] = i
    else:
        max_size = max(max_size, len(arr) - start)
        return max_size


assert size_distinct([]) == 0
assert size_distinct([1]) == 1
assert size_distinct(['a', 'a']) == 1
assert size_distinct(['a', 'b', 'c', 'd']) == 4

assert size_distinct(['a', 'b', 'c', 'b', 'd', 'c', 'a', 'd', 'a']) == 4
assert size_distinct(['a', 'b', 'c', 'b', 'd', 'a']) == 4
assert size_distinct(['a', 'b', 'c', 'b', 'd', 'b', 'a']) == 3

assert size_distinct([5, 1, 3, 5, 2, 3, 4, 1]) == 5
