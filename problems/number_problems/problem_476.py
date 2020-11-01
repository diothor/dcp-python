from typing import List, Union


# O(n)
def duplicate(nums: List[int]) -> Union[int, None]:
    nums_len = len(nums)                                # O(1)
    if nums_len < 2:
        return None
    else:
        expected_sum = (nums_len - 1) * nums_len // 2   # O(1)
        actual_sum = sum(nums)                          # O(n)
        return actual_sum - expected_sum


assert duplicate([]) is None
assert duplicate([0]) is None

assert duplicate([1, 3, 2, 3]) == 3
assert duplicate(list(range(1, 201)) + [67]) == 67
