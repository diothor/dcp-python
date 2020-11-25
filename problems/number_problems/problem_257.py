from typing import Optional, Tuple


# O(n)
def find_unsorted_part(*unsorted_list) -> Tuple[Optional[int], Optional[int]]:
    size = len(unsorted_list)

    vmax = float('-inf')
    vmin = float('inf')

    istart = None
    iend = None
    for i in range(size):
        if unsorted_list[i] > vmax:
            vmax = unsorted_list[i]
        elif unsorted_list[i] < vmax:
            iend = i

        if unsorted_list[size - 1 - i] < vmin:
            vmin = unsorted_list[size - 1 - i]
        elif unsorted_list[size - 1 - i] > vmin:
            istart = size - 1 - i

    return istart, iend


assert find_unsorted_part() == (None, None)
assert find_unsorted_part(100) == (None, None)

assert find_unsorted_part(1, 2, 3) == (None, None)
assert find_unsorted_part(3, 2, 1) == (0, 2)

assert find_unsorted_part(3, 7, 5, 6, 9) == (1, 3)
assert find_unsorted_part(10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60) == (3, 8)
assert find_unsorted_part(0, 1, 15, 25, 6, 7, 30, 40, 50) == (2, 5)

assert find_unsorted_part(1, 2, 4, 8, 3, 7, 9) == (2, 5)
