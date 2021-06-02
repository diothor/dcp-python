# O(n) where n is length of arr
def longest_of_k(arr: list, k: int = 2) -> int:
    if k < 1 or arr is None:
        return 0

    longest = 0
    start_index = 0
    end_index = 0
    element_set = {}
    element_count = 0

    while end_index < len(arr):
        if element_count < k or arr[end_index] in element_set:
            element = arr[end_index]
            element_set[element] = element_set.setdefault(element, 0) + 1
            end_index += 1
            element_count = min(element_count + 1, k)
        else:
            longest = max(longest, end_index - start_index)
            element = arr[start_index]
            if element_set.get(element) == 1:
                del element_set[element]
                element_count -= 1
            else:
                element_set[element] -= 1
            start_index += 1
    else:
        return max(longest, end_index - start_index)


# basic cases
assert longest_of_k([]) == 0
assert longest_of_k(['A']) == 1
assert longest_of_k(['A', 'A']) == 2
assert longest_of_k(['A', 'B']) == 2
assert longest_of_k(['A', 'B', 'C']) == 2

assert longest_of_k([], 0) == 0
assert longest_of_k(['V'], 0) == 0
assert longest_of_k(['A', 'B', 'C'], 1) == 1
assert longest_of_k(['A', 'B', 'C'], 2) == 2
assert longest_of_k(['A', 'B', 'C'], 3) == 3
assert longest_of_k(['A', 'B', 'C'], 4) == 3

assert longest_of_k(['V'], -1) == 0

assert longest_of_k([2, 1, 2, 3, 3, 1, 3, 5]) == 4
assert longest_of_k([1, 2, 3, 4, 5]) == 2
assert longest_of_k([6, 5, 1, 2, 3, 2, 1, 4, 5], 3) == 5
