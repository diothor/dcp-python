# O(n) where n is number of bits of max value from XOR and AND of values in pair
def pairs(my_sum: int, my_xor: int) -> int:
    if (my_sum ^ my_xor) & 1 == 1:
        return 0

    my_and = (my_sum - my_xor) // 2
    pair_count = 1
    bit = 1
    while my_sum >= bit or my_and >= bit:
        xi = my_xor & bit
        ai = my_and & bit
        if xi == bit and ai == 0:
            pair_count *= 2
        bit <<= 1
    else:
        return pair_count


assert pairs(17, 13) == 8
assert pairs(1639, 1176) == 0
assert pairs(100, 4) == 2
assert pairs(4, 0) == 1
