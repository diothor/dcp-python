from typing import Tuple
from operator import itemgetter


# O(nlogn)
def rooms(*classes: Tuple[int, int]) -> int:
    # 3*O(n) + 2*O(nlogn) ~= O(nlogn)
    classes = [(s, t) for s, t in classes if s < t]  # O(n)
    n = len(classes)
    starts = sorted(map(itemgetter(0), classes))  # O(n) + O(nlogn)
    ends = sorted(map(itemgetter(1), classes))  # O(n) + O(nlogn)

    max_rooms, current_rooms = 0, 0
    index_s, index_e = 0, 0

    # O(2n) ~= O(n)
    while index_s < n:
        if starts[index_s] < ends[index_e]:
            current_rooms += 1
            index_s += 1
            max_rooms = max(max_rooms, current_rooms)
        elif starts[index_s] >= ends[index_e]:
            current_rooms -= 1
            index_e += 1
    else:
        return max_rooms


# non-overlaping example
assert rooms((1, 2), (2, 3), (3, 4), (4, 5)) == 1

# given examples
assert rooms((30, 75), (0, 50), (60, 150)) == 2
assert rooms((900, 910), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)) == 3

# checking wrong data when a meeting starts after it has ended
assert rooms((1, 2)) == 1
assert rooms((2, 1)) == 0
assert rooms((5, 1), (2, 4), (2, 1), (1, 3)) == 2
