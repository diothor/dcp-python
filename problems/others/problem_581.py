from typing import Tuple


def corners(left_top, width_height) -> Tuple[int, int, int, int]:
    left, top = left_top
    width, height = width_height
    right, bottom = left + width, top - height
    return left, top, right, bottom


def intersection_area(a_left_top: Tuple[int, int], a_dimensions: Tuple[int, int], b_left_top: Tuple[int, int], b_dimensions: Tuple[int, int]) -> int:
    a_left, a_top, a_right, a_bottom = corners(a_left_top, a_dimensions)
    b_left, b_top, b_right, b_bottom = corners(b_left_top, b_dimensions)
    return abs(max(a_left, b_left) - min(a_right, b_right)) * abs(min(a_top, b_top) - max(a_bottom, b_bottom))


# from the task
assert intersection_area((1, 4), (3, 3), (0, 5), (4, 3)) == 6
# one inside another
assert intersection_area((1, 1), (4, 5), (2, 0), (2, 3)) == 6
# no intersection
assert intersection_area((-1, -1), (3, 3), (2, 1), (5, 6)) == 0
