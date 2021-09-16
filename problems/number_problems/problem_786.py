from typing import Union


# O(logn)
def my_pow(base: int, power: int) -> Union[int, float]:
    if power == 0 or base == 1:
        return 1
    elif base == 0:
        return 0

    half = my_pow(base, int(power / 2))
    if power % 2 == 0:
        return half * half
    elif power > 0:
        return base * half * half
    else:
        return half * half / base


assert my_pow(0, 10) == 0
assert my_pow(7, 0) == 1
assert my_pow(1, 100) == 1

assert my_pow(2, 2) == 4
assert my_pow(2, 3) == 8

assert my_pow(3, 4) == 81
assert my_pow(5, 3) == 125
assert my_pow(2, 10) == 1024

assert my_pow(0, -1) == 0
assert my_pow(1, -10) == 1
assert my_pow(2, -1) == 0.5
assert my_pow(2, -3) == 0.125
assert my_pow(2, -2) == 1/4
assert 0.007 < my_pow(5, -3) < 0.009
