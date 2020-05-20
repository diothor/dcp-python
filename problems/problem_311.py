def peak_element(arr: list, start=0, end=None) -> int or None:
    if end is None:
        end = len(arr) - 1

    midd = (end + start) // 2
    if end - 1 < midd < start + 1:
        return None

    prev_e, elem, next_e = arr[midd - 1:midd + 2]
    if prev_e < elem > next_e:
        return elem
    elif next_e > elem:
        return peak_element(arr, start=midd)
    elif prev_e > elem:
        return peak_element(arr, end=midd)


assert peak_element([]) is None
assert peak_element([0, 1, 1, 0]) is None
assert peak_element([0, 1, 0]) == 1
assert peak_element([5, 10, 20, 15]) == 20
assert peak_element([10, 20, 15, 2, 23, 90, 67]) in [20, 90]
