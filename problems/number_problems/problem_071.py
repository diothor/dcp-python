from random import randint
from collections import Counter


def rand7() -> int:
    return randint(1, 7)


def rand5() -> int:
    res = rand7()
    return res if res < 6 else rand5()


values = [rand5() for _ in range(50000)]

stats = Counter(values)
assert len(stats) == 5
assert all([9700 < v < 10300 for v in stats.values()])
