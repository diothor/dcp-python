from typing import List


# O(n)
def max_triplet_product(nums: List[int]) -> int:
    size = len(nums)
    if size < 3:
        raise ValueError()

    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for n in nums:
        if n > max1:
            max3, max2, max1 = max2, max1, n
        elif n > max2:
            max3, max2 = max2, n
        elif n > max3:
            max3 = n

        if n < min1:
            min2, min1 = min1, n
        elif n < min2:
            min2 = n
    else:
        return max(max1 * max2 * max3, min1 * min2 * max1)


assert max_triplet_product([-10, -10, 5, 2]) == 500

assert max_triplet_product([-10, 2, 3, 4]) == 24
assert max_triplet_product([-10, 2, -3, 4]) == 120
assert max_triplet_product([-1, 2, -3, 4]) == 12
assert max_triplet_product([10, 2, 3, 4]) == 120
assert max_triplet_product([-10, -3, -5, -6, -20]) == -90

assert max_triplet_product([10, 3, 5, 6, 20]) == 1200
assert max_triplet_product([1, -4, 3, -6, 7, 0]) == 168
