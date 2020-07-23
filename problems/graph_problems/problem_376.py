from typing import Tuple, List, Union
from math import sqrt


# O(n) - I assume the coins don't need to be sorted
def closes_coin(position: Tuple[int, int], coins: List[Tuple[int, ...]]) -> Union[Tuple[int, int], None]:
    my_x, my_y = position
    min_dist: float = float('inf')
    closest = None
    for c_x, c_y in coins:
        dist = sqrt((c_x - my_x)**2 + (c_y - my_y)**2)
        if dist < min_dist:
            min_dist = dist
            closest = (c_x, c_y)
    else:
        return closest


assert closes_coin((0, 2), [(0, 4), (1, 0), (2, 0), (3, 2)]) == (0, 4)
