from math import log2


# O(logn)
def sevenish(n: int) -> int:
    if n == 0:
        return 0
    k = int(log2(n))
    return 7 ** k + sevenish(n - 2 ** k)


assert sevenish(1) == 7 ** 0
assert sevenish(2) == 7 ** 1
assert sevenish(3) == 7 ** 0 + 7 ** 1
assert sevenish(4) == 7 ** 2
assert sevenish(5) == 7 ** 0 + 7 ** 2
assert sevenish(6) == 7 ** 1 + 7 ** 2
assert sevenish(7) == 7 ** 0 + 7 ** 1 + 7 ** 2

assert sevenish(11) == 351
assert sevenish(15) == 400
