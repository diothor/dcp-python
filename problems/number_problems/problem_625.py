# O(n) where n is number of bits in num
def consecutive_ones(num: int) -> int:
    max_count, current_count = 0, 0
    while num > 0:
        last_bit = num & 1
        current_count += last_bit
        if last_bit != 1:
            max_count = max(max_count, current_count)
            current_count = 0
        num >>= 1
    else:
        return max(max_count, current_count)


assert consecutive_ones(0) == 0
assert consecutive_ones(1) == 1
assert consecutive_ones(2) == 1
assert consecutive_ones(3) == 2
assert consecutive_ones(11) == 2

assert consecutive_ones(156) == 3
assert consecutive_ones(7) == 3
