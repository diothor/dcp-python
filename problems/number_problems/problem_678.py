from typing import List
from functools import reduce


def to_digits(num: int) -> List[int]:
    digits = []
    while num > 10:
        digits.append(num % 10)
        num //= 10
    else:
        digits.append(num)
        digits.reverse()
        return digits


def to_int(digits: List[int]) -> int:
    return reduce(lambda num, d: num * 10 + d, digits, 0)


# O(n)
def next_perm(num: int) -> int:
    digits = to_digits(num)
    size = len(digits)
    swap_to, swap_from = None, None

    # O(n)
    for i in range(size - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            swap_to, swap_from = i - 1, i
            break
    else:
        return num

    # O(n)
    for i in range(swap_from, size):
        if digits[swap_to] < digits[i] <= digits[swap_from]:
            swap_from = i

    digits[swap_to], digits[swap_from] = digits[swap_from], digits[swap_to]
    # O(n)
    digits[swap_to + 1:] = sorted(digits[swap_to + 1:])
    return to_int(digits)


assert next_perm(1) == 1
assert next_perm(11) == 11
assert next_perm(12) == 21
assert next_perm(21) == 21

assert next_perm(321) == 321
assert next_perm(123) == 132
assert next_perm(1243) == 1324

assert next_perm(48975) == 49578
