from typing import List


# O(n)
def regular_numbers(n: int) -> List[int]:
    nums: List[int] = [1]
    nums_size = 1

    next_values = [2, 3, 5]
    next_indexes = [0, 0, 0]

    while nums_size < n:
        next_num = min(next_values)
        nums.append(next_num)
        nums_size += 1
        if next_num == next_values[0]:
            next_indexes[0] += 1
            next_values[0] = 2 * nums[next_indexes[0]]
        if next_num == next_values[1]:
            next_indexes[1] += 1
            next_values[1] = 3 * nums[next_indexes[1]]
        if next_num == next_values[2]:
            next_indexes[2] += 1
            next_values[2] = 5 * nums[next_indexes[2]]
    else:
        return nums if n > 0 else []


assert regular_numbers(0) == []
assert regular_numbers(5) == [1, 2, 3, 4, 5]
assert regular_numbers(10) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
assert regular_numbers(62) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243,
                               250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405]
