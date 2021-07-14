from typing import List
from operator import itemgetter


# O(nlogn) where n is number of intervals
def common_numbers(*intervals: List[int]) -> set:
    intervals = sorted(intervals, key=itemgetter(1, 0))
    print(intervals)
    nums = []
    for start, end in intervals:
        if not nums or start > nums[-1]:
            nums.append(end)
    else:
        return set(nums)


assert common_numbers([0, 3], [2, 6], [3, 4], [6, 9]) == {3, 9}
assert common_numbers([0, 4], [1, 2], [5, 7], [6, 7], [6, 9], [8, 10]) == {2, 7, 10}
