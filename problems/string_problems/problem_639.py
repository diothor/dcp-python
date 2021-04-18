from typing import List, Callable
from collections import deque


def digit2chars(d: int) -> List[str]:
    if d < 2:
        return []
    else:
        first_code = 91 + d * 3 + (d > 7)
        last_code = first_code + 3 + (d == 7 or d == 9)
        return [chr(code) for code in range(first_code, last_code)]


assert digit2chars(1) == []
assert digit2chars(0) == []

assert digit2chars(2) == ['a', 'b', 'c']
assert digit2chars(3) == ['d', 'e', 'f']
assert digit2chars(8) == ['t', 'u', 'v']

assert digit2chars(7) == ['p', 'q', 'r', 's']
assert digit2chars(9) == ['w', 'x', 'y', 'z']


# O(C^n) - expotential; where n is length of the num string
def num2str(num: str, mapping: Callable[[int], List[int]] = digit2chars) -> list:
    num_size = len(num)
    empty_digits = 0
    res: list = []
    queue: deque = deque([''])
    while queue:
        base = queue.pop()
        curr_size = len(base) + empty_digits
        if curr_size == num_size:
            res.append(base)
        else:
            digit = int(num[curr_size])
            letters = mapping(digit)
            if letters:
                queue.extendleft(map(lambda let: base + let, letters))
            else:
                empty_digits += 1
                queue.append(base)
    else:
        return res


# test from DCP
assert num2str('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# 4 character digits
assert num2str('78') == ['pt', 'pu', 'pv', 'qt', 'qu', 'qv', 'rt', 'ru', 'rv', 'st', 'su', 'sv']
assert num2str('49') == ['gw', 'gx', 'gy', 'gz', 'hw', 'hx', 'hy', 'hz', 'iw', 'ix', 'iy', 'iz']

# no character digits
assert num2str('010') == ['']
assert num2str('51') == ['j', 'k', 'l']
assert num2str('15') == ['j', 'k', 'l']
