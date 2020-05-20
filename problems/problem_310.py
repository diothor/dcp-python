def count_set_bits(num: int) -> int:
    nbits = 0
    while (num >> nbits) > 0:  # O(n)
        nbits += 1

    # O(n+1) * O(logn)
    ones = 0
    for bit_i in range(nbits):  # O(nbits) = O(logn)
        flip_cycle = 1 << bit_i
        bit_v = 0
        for i in range(num + 1):  # O(n+1)
            if i and i % flip_cycle == 0:
                bit_v = not bit_v
            ones += bit_v
    return ones


assert count_set_bits(0) == 0
assert count_set_bits(1) == 1
assert count_set_bits(3) == 4
assert count_set_bits(6) == 9
assert count_set_bits(7) == 12
assert count_set_bits(8) == 13
assert count_set_bits(9) == 15
