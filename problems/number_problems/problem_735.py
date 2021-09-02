from typing import Optional


# O(logn) where n is number of elements in the arr
def peak(*arr: int, start: int = 0, end: int = None) -> Optional[int]:
    if end is None:
        end = max(len(arr) - 1, start)  # len() has O(n) time complexity, so end value should be always passed to peak() as an argument. Here we set it just once and just for convenience.
    if end < start:
        return None

    mid_index = (end + start) // 2
    potential_peak = arr[mid_index]
    value_on_left = arr[mid_index - 1] if mid_index > 0 else float('-inf')
    value_on_right = arr[mid_index + 1] if mid_index < len(arr) - 1 else float('-inf')

    if value_on_left < potential_peak > value_on_right:
        return potential_peak
    elif value_on_left > potential_peak:
        return peak(*arr, start=start, end=mid_index - 1)
    elif value_on_right > potential_peak:
        return peak(*arr, start=mid_index + 1, end=end)
    else:
        peak_value = peak(*arr, start=start, end=mid_index - 1)
        return peak_value if peak_value is not None else peak(*arr, start=mid_index + 1, end=end)


# basic test cases
assert peak(1, 1, 1) is None
assert peak(1, 2, 1) == 2
assert peak(1, 2, 2, 1) is None

# testing repeating values
assert peak(1, 1, 2, 1) == 2
assert peak(1, 1, 1, 2, 1) == 2
assert peak(1, 2, 1, 1, 1, 1, 1) == 2

# testing peaks at the border
assert peak(1, 1) is None
assert peak(3, 8) == 8
assert peak(8, 3) == 8

# geekforgeeks acceptance tests
assert peak(5, 10, 20, 15) == 20
assert peak(10, 20, 15, 2, 23, 90, 67) in {20, 90}
