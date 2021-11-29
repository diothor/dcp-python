from typing import List, Union
from heapq import *


class HeapWithMultiplier:

    def __init__(self, multiplier: int):
        self._multiplier = multiplier
        self._heap = []
        self._size = 0

    def size(self):
        return self._size

    def push(self, val):
        heappush(self._heap, self._multiplier * val)
        self._size += 1

    def pop(self):
        self._size -= 1
        return self._multiplier * heappop(self._heap)

    def peek(self):
        return self._multiplier * self._heap[0]

    def replace(self, val):
        return self._multiplier * heapreplace(self._heap, self._multiplier * val)


class MaxHeap(HeapWithMultiplier):

    def __init__(self):
        super().__init__(-1)


class MinHeap(HeapWithMultiplier):

    def __init__(self):
        super().__init__(1)


# O(nlogn)
def running_median(*nums: int) -> List[Union[int, float]]:
    medians = []
    current_median = 0

    lower_half = MaxHeap()
    higher_half = MinHeap()

    for n in nums:  # O(n)
        has_been_odd = lower_half.size() != higher_half.size()

        # update the heaps
        if lower_half.size() > higher_half.size():
            above_median = n
            if above_median < current_median:
                above_median = lower_half.replace(n)  # O(logn)
            higher_half.push(above_median)  # O(logn)
        elif lower_half.size() < higher_half.size():
            below_median = n
            if below_median > current_median:
                below_median = higher_half.replace(n)  # O(logn)
            lower_half.push(below_median)  # O(logn)
        else:
            if n > current_median:
                higher_half.push(n)  # O(logn)
            else:
                lower_half.push(n)  # O(logn)

        # calculate the current median
        if has_been_odd:
            current_median = (lower_half.peek() + higher_half.peek()) / 2
        else:
            current_median = (higher_half if higher_half.size() > lower_half.size() else lower_half).peek()
        medians.append(current_median)
    else:
        return medians


assert running_median() == []
assert running_median(2) == [2]
assert running_median(2, 1) == [2, 1.5]
assert running_median(2, 1, 5) == [2, 1.5, 2]

assert running_median(2, 1, 5, 7, 2, 0, 5) == [2, 1.5, 2, 3.5, 2, 2, 2]
