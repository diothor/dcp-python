from typing import Optional
from math import log2, ceil


# O(1)
def throws_to_single_head(coins: int) -> Optional[int]:
    return None if coins < 1 else ceil(log2(coins))


assert throws_to_single_head(1) == 0
assert throws_to_single_head(2) == 1
assert throws_to_single_head(6) == 3
assert throws_to_single_head(1025) == 11

assert throws_to_single_head(0) is None
assert throws_to_single_head(-1) is None
