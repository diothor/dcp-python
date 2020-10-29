# O(n)
def decode_count(coded: str) -> int:
    possibilities = 1
    for index in range(len(coded)):  # O(n)
        two_dig = int(coded[index:index + 2])  # O(1)
        if 9 < two_dig < 27:
            possibilities += 1
    else:
        return possibilities - coded.count('0')


assert decode_count('') == 1
assert decode_count('1') == 1

assert decode_count('18') == 2
assert decode_count('38') == 1

assert decode_count('111') == 3
assert decode_count('131') == 2

assert decode_count('1234') == 3
assert decode_count('121') == 3

assert decode_count('10') == 1
assert decode_count('101') == 1
assert decode_count('10101') == 1
assert decode_count('10111') == 3  # jaaa, jka, jak
