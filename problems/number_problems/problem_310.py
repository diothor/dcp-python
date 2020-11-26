# O(1)
def pow2(exponent: int) -> int:
    return 1 << exponent


# O(logn)
def bits_size(val: int) -> int:
    bits = 0
    while val > 1:
        bits += 1
        val = val >> 1
    else:
        return bits


# O((logn)^2) - polylogarithmic
def count_set_bits(num: int) -> int:
    if num < 1:
        return 0
    highest_bit = bits_size(num)
    num_of_bits = highest_bit + 1
    if num == pow2(num_of_bits) - 1:
        return num_of_bits * pow2(highest_bit)
    else:
        num_rest = num - pow2(highest_bit)
        return (num + 1 - pow2(num_of_bits - 1)) + (num_of_bits - 1) * pow2(highest_bit - 1) + count_set_bits(num_rest)


assert count_set_bits(0) == 0
assert count_set_bits(1) == 1
assert count_set_bits(3) == 4
assert count_set_bits(4) == 5
assert count_set_bits(6) == 9
assert count_set_bits(7) == 12
assert count_set_bits(8) == 13
assert count_set_bits(9) == 15
assert count_set_bits(12345) == 82199
