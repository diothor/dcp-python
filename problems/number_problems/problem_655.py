# O(n) where n is number of bits in num
def reversed_num(num: int) -> int:
    rev = 0
    while num > 0:
        rev <<= 1
        rev ^= num & 1
        num >>= 1
    else:
        return rev


# base cases
assert reversed_num(0) == 0
assert reversed_num(1) == 1
assert reversed_num(0b10) == 0b01
assert reversed_num(0b11) == 0b11

# geek for geeks
assert reversed_num(10) == 5
assert reversed_num(11) == 13

# acceptance cases
assert reversed_num(0b11110000111100001111000011110000) == 0b00001111000011110000111100001111
