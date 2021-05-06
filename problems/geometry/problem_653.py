from operator import itemgetter


# O(1)
def pair_overlaps(left, right) -> bool:
    left_x_min, left_x_max, left_y_min, left_y_max = left
    right_x_min, right_x_max, right_y_min, right_y_max = right
    return left_x_min <= right_x_min and left_x_max >= right_x_max and left_y_min <= right_y_min and left_y_max >= right_y_max


# O(n^2) where n is number of rectangles
def has_overlap(rectangles) -> bool:
    rectangles.sort(key=itemgetter(0))
    size = len(rectangles)
    for left in range(size):
        for right in range(left+1, size):
            if pair_overlaps(rectangles[left], rectangles[right]):
                return True
    else:
        return False


# simple cases
assert has_overlap([]) is False
assert has_overlap([(2, 8, 2, 8), (3, 7, 3, 7)])  # two rectangles one into the other
assert has_overlap([(1, 3, 2, 5), (1, 3, 2, 5)])  # two the same rectangles
assert has_overlap([(1, 3, 1, 4), (5, 10, 2, 3)]) is False  # two rectangles next to each other horizontally

# acceptance case
assert has_overlap([(1, 4, 1, 4), (-1, 1, 2, 3), (0, 4, 1, 5)]) is True
