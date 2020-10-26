from typing import Union


# O(n)
def closest_larger(arr: list, i: int) -> Union[int, None]:
    if not -1 < i < len(arr):
        return None

    distance = 1
    while i + distance < len(arr) or i - distance > -1:
        if i - distance > -1 and arr[i - distance] > arr[i]:
            return i - distance
        elif i + distance < len(arr) and arr[i + distance] > arr[i]:
            return i + distance
        else:
            distance += 1
    else:
        return None


# test from the task
# assert closest_larger([4, 1, 3, 5, 6], 0) == 3

# tests from https://stackoverflow.com/questions/25812382/how-to-find-the-nearest-larger-element-to-another-element-in-an-array
# assert closest_larger([1, 2, 6, 5, 10], 0) == 1
# assert closest_larger([1, 2, 6, 5, 10], 1) == 2
# assert closest_larger([1, 2, 6, 5, 10], 2) == 4
assert closest_larger([1, 2, 6, 5, 10], 3) in (2, 4)
assert closest_larger([1, 2, 6, 5, 10], 4) is None

# check when larger number in equal distance on both sides
assert closest_larger([2, 0, 1, -8, 2], 2) in (0, 4)

# check when no larger number
assert closest_larger([1, 2, 3], 2) is None

# check when empty array
assert closest_larger([], 2) is None

# check right when left found
assert closest_larger([7, 1, 3, 4], 2) == 3
