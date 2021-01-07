# O(n*k)
def rotate_right(arr: list, k: int) -> list:
    n = len(arr)
    k %= n
    for item in range(-k, 0):
        stop = item - n + k
        while item > stop:
            arr[item], arr[item - 1] = arr[item - 1], arr[item]
            item -= 1
    else:
        return arr


assert rotate_right([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert rotate_right([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
assert rotate_right([1, 2, 3, 4, 5], 9) == [2, 3, 4, 5, 1]
assert rotate_right([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
assert rotate_right([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]

assert rotate_right([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
assert rotate_right([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3]
assert rotate_right([1, 2, 3, 4, 5, 6], 4) == [3, 4, 5, 6, 1, 2]
