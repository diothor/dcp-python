def find_not_subsum(arr: list) -> int:
    if arr[0] != 1:
        return 1

    max_potential_num = 1
    for n in arr[1:]:
        if n <= max_potential_num + 1:
            max_potential_num += n
        else:
            return max_potential_num + 1
    else:
        return max_potential_num + 1


assert find_not_subsum([1]) == 2
assert find_not_subsum([1, 1, 1, 1, 1]) == 6
assert find_not_subsum([1, 2, 3, 10]) == 7
assert find_not_subsum([2, 3, 6, 7]) == 1
assert find_not_subsum([1, 2, 6, 7, 9]) == 4
assert find_not_subsum([1, 1, 3, 4, 6, 7, 9]) == 32
