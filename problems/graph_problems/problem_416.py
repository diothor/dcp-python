from typing import List, Tuple


# O(n)
def steps_in_order(points: List[Tuple[int, int]]) -> int:
    result = 0
    for a, b in zip(points, points[1:]):
        diff_x = abs(a[0] - b[0])
        diff_y = abs(a[1] - b[1])
        result += max(diff_x, diff_y)
    else:
        return result


assert steps_in_order([(1, 1), (1, 1)]) == 0
assert steps_in_order([(0, 0), (1, 1), (1, 2)]) == 2
assert steps_in_order([(0, 0), (-1, -1), (-1, -2)]) == 2
assert steps_in_order([(4, 6), (1, 2), (4, 5), (10, 12)]) == 14
