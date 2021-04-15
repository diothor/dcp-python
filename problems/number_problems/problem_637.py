from typing import List, Tuple
from operator import itemgetter


# O(nlogn)
def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    intervals.sort(key=itemgetter(0))  # O(nlogn)
    merged = []
    start, end = intervals[0]

    for current in intervals[1:]:  # O(n)
        if current[0] > end:
            merged.append((start, end))
            start, end = current
        elif current[1] > end:
            end = current[1]
    else:
        merged.append((start, end))

    return merged


assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
assert merge_intervals([(1, 3), (2, 4), (5, 7), (6, 8)]) == [(1, 4), (5, 8)]
