from collections import deque
from typing import List


def num_to_base(num: int, base: int) -> List[int]:
    if num < 0:
        return []
    elif num == 0:
        return [0]

    bits = deque()
    while num > 0:
        bits.appendleft(num % base)
        num = num // base
    else:
        return list(bits)


def skip_zero(bits: List[int], base: int) -> None:
    for index in range(len(bits) - 1, 0, -1):
        if bits[index] < 1:
            bits[index - 1] -= 1
            bits[index] += base


def alphabetical_id(col: int) -> str:
    char_count = 26
    base26bits = num_to_base(col, char_count)
    skip_zero(base26bits, char_count)

    char_offset = 64
    return ''.join(map(lambda b: chr(char_offset + b), filter(lambda b: b > 0, base26bits)))


assert alphabetical_id(1) == 'A'
assert alphabetical_id(27) == 'AA'

assert alphabetical_id(2) == 'B'
assert alphabetical_id(25) == 'Y'
assert alphabetical_id(26) == 'Z'

assert alphabetical_id(28) == 'AB'
assert alphabetical_id(2 * 26) == 'AZ'
assert alphabetical_id(2 * 26 + 1) == 'BA'

assert alphabetical_id(26 * 26 * 2 + 26 * 4 + 3) == 'BDC'

# from geeksforgeeks
assert alphabetical_id(26) == 'Z'
assert alphabetical_id(51) == 'AY'
assert alphabetical_id(52) == 'AZ'
assert alphabetical_id(80) == 'CB'
assert alphabetical_id(676) == 'YZ'
assert alphabetical_id(702) == 'ZZ'
assert alphabetical_id(705) == 'AAC'
