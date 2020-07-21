from typing import Union


# O(logn)
def magic_index(sorted_nums: list, start: int = 0, end: int = None) -> Union[int, None]:
    if end is None:
        end = len(sorted_nums)
    if start == end:
        return None

    midd_index = (start + end) // 2
    midd_value = sorted_nums[midd_index] if midd_index < len(sorted_nums) else None
    if midd_index > midd_value:
        return magic_index(sorted_nums, midd_index + 1, end)
    elif midd_index < midd_value:
        return magic_index(sorted_nums, 0, midd_index)
    else:
        prev = magic_index(sorted_nums, 0, midd_index)
        return midd_index if prev is None else min(midd_index, prev)


assert magic_index([]) is None
assert magic_index([4, 6]) is None
assert magic_index([-4, -2]) is None
assert magic_index([-5, -3, 2, 3]) == 2
assert magic_index([-5, -3, 0, 3, 4]) == 3
assert magic_index([-5, 1, 2, 3]) == 1
assert magic_index([0, 1, 2, 3]) == 0
