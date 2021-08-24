# O(n*k)
def rotate_left(arr: list, k: int) -> list:
    size = len(arr)
    k %= size
    for to_move in range(k - 1, -1, -1):
        for shift in range(size - k):
            arr[to_move + shift], arr[to_move + 1 + shift] = arr[to_move + 1 + shift], arr[to_move + shift]
    else:
        return arr


# basic cases
assert rotate_left([1, 2], 1) == [2, 1]
assert rotate_left([1, 2], 2) == [1, 2]
assert rotate_left([1, 2], 3) == [2, 1]

assert rotate_left([1, 2, 3], 1) == [2, 3, 1]
assert rotate_left([1, 2, 3], 2) == [3, 1, 2]

# acceptance cases
assert rotate_left([1, 2, 3, 4, 5, 6], 1) == [2, 3, 4, 5, 6, 1]
assert rotate_left([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]

assert rotate_left([1, 2, 3, 4, 5, 6], 4) == [5, 6, 1, 2, 3, 4]
assert rotate_left([1, 2, 3, 4, 5, 6], 5) == [6, 1, 2, 3, 4, 5]

assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5) == [6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5]
assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 7) == [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
