from typing import List


# O(n)
def max_triplet_product(nums: List[int]) -> int:
    size = len(nums)
    if size < 3:
        raise ValueError()

    max_on_left = [float('-inf')] * size
    min_on_left = [float('inf')] * size

    max_on_right = [float('-inf')] * size
    min_on_right = [float('inf')] * size

    for i in range(size):
        if i > 0:
            max_on_left[i] = max(max_on_left[i - 1], nums[i - 1])
            min_on_left[i] = min(min_on_left[i - 1], nums[i - 1])
        if i < size - 1:
            max_on_right[i] = max(max_on_right[i + 1], nums[i + 1])
            min_on_right[i] = min(min_on_right[i + 1], nums[i + 1])

    max_prod = float('-inf')
    for i in range(1, size - 1):
        prod_from_negative = min_on_left[i] * nums[i] * min_on_right[i]
        prod_from_positive = max_on_left[i] * nums[i] * max_on_right[i]
        max_prod = max(max_prod, prod_from_positive, prod_from_negative)
    else:
        return max_prod


assert max_triplet_product([-10, -10, 5, 2]) == 500

assert max_triplet_product([-10, 2, 3, 4]) == 24
assert max_triplet_product([-10, 2, -3, 4]) == 120
assert max_triplet_product([-1, 2, -3, 4]) == 12
assert max_triplet_product([10, 2, 3, 4]) == 120
assert max_triplet_product([-10, -3, -5, -6, -20]) == -90

assert max_triplet_product([10, 3, 5, 6, 20]) == 1200
assert max_triplet_product([1, -4, 3, -6, 7, 0]) == 168
