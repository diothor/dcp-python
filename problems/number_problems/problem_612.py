from operator import itemgetter


# O(nlogn)
def num_to_non_overlapping(intervals: list) -> int:
    intervals.sort(key=itemgetter(0))
    count = 0
    prev_start, prev_end = (0, 0)
    for curr_start, curr_end in intervals:
        if prev_end <= curr_start:
            prev_start, prev_end = curr_start, curr_end
        else:
            count += 1
            if prev_end < curr_end:
                prev_start, prev_end = curr_start, curr_end
    else:
        return count


assert num_to_non_overlapping([(7, 9), (2, 4), (5, 8)]) == 1

assert num_to_non_overlapping([]) == 0
assert num_to_non_overlapping([(0, 1), (1, 2), (2, 3), (5, 10)]) == 0

assert num_to_non_overlapping([(1, 2), (4, 7), (3, 8)]) == 1
assert num_to_non_overlapping([(10, 20), (10, 20), (10, 20)]) == 2
assert num_to_non_overlapping([(1, 2), (5, 10), (18, 35), (40, 45)]) == 0
