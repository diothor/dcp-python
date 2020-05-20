def peak_element(arr: list) -> int or None:
    # O(n)
    for i in range(1, len(arr) - 1):
        prev_e, elem, next_e = arr[i - 1:i + 2]
        if prev_e < elem > next_e:
            return elem
    else:
        return None


assert peak_element([]) is None
assert peak_element([0, 1, 1, 0]) is None
assert peak_element([5, 10, 20, 15]) == 20
assert peak_element([10, 20, 15, 2, 23, 90, 67]) in [20, 90]
