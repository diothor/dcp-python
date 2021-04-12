from typing import List


# O(logn) where n is length of arr
def min_in_pivot(arr: List[int], st: int = 0, end: int = None) -> int:
    if end is None:
        end = len(arr) - 1

    mid = (st + end) // 2
    if mid >= end:
        return None if end < 0 else arr[0]
    if arr[mid] > arr[mid + 1]:
        return arr[mid + 1]

    if arr[st] > arr[mid]:
        return min_in_pivot(arr, st, mid)
    else:
        return min_in_pivot(arr, mid + 1, end)


assert min_in_pivot([5, 7, 10, 3, 4]) == 3
assert min_in_pivot([5, 6, 7, 8, 9, 10, 1, 2, 3]) == 1
assert min_in_pivot([30, 40, 50, 10, 20]) == 10

assert min_in_pivot([3, 4, 1, 2]) == 1
assert min_in_pivot([4, 1, 2, 3]) == 1
assert min_in_pivot([2, 3, 4, 1]) == 1

assert min_in_pivot([3, 4, 5, 1, 2]) == 1
assert min_in_pivot([4, 5, 1, 2, 3]) == 1
assert min_in_pivot([2, 3, 4, 5, 1]) == 1

assert min_in_pivot([20, 10]) == 10

assert min_in_pivot([2, 3, 4, 5, 6]) == 2
assert min_in_pivot([100]) == 100
assert min_in_pivot([]) is None

assert min_in_pivot([10, 10, 10, 10, 5, 5]) == 5
assert min_in_pivot([10, 10, 5, 5, 5]) == 5
assert min_in_pivot([10, 10, 10, 10]) == 10
assert min_in_pivot([10, 10]) == 10
