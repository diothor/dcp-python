def next_int(n: int) -> int:
    bits = list(f'0{n:b}')  # adding 0 before number takes care of no-0 bit case
    rmb = len(bits) - 1  # index of the right most bit
    ones = 0 if bits[rmb] == '0' else 1
    for i in range(rmb - 1, -1, -1):
        if bits[i] == '0' and bits[i + 1] == '1':
            bits[i:] = ['1'] + ['0'] * (rmb - i - ones + 1) + ['1'] * (ones - 1)
            break
        elif bits[i] == '1':
            ones += 1
    return int(''.join(bits), 2)


assert next_int(0b1) == 0b10
assert next_int(0b11) == 0b101

assert next_int(0b1111) == 0b10111

assert next_int(0b10011100) == 0b10100011
assert next_int(0b11011001111100) == 0b11011010001111
