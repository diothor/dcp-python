from operator import itemgetter
from heapq import heappop, heappush


def max_overlap(intervals: list) -> int:
    intervals.sort(key=itemgetter(0, 1))

    end_times = []
    overlaps = 0
    for i in intervals:
        while end_times and end_times[0] < i[0]:
            heappop(end_times)
        heappush(end_times, i[1])
        overlaps = max(overlaps, len(end_times))

    return overlaps if overlaps > 1 else 0


lectures = [(30, 75), (0, 50), (60, 150)]
assert max_overlap(lectures) == 2
