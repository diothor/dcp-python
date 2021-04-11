from typing import List, Optional


# O(n^2)
def coins_in_use(ways_for_change: List[int]) -> List[int]:
    size = len(ways_for_change)
    coins = []

    def find_lowest() -> Optional[int]:  # O(n)
        try:
            return ways_for_change.index(1, 1)
        except ValueError:
            return None

    lowest = find_lowest()
    while lowest:  # O(n)
        coins.append(lowest)
        for i in reversed(range(lowest, size)):  # O(n)
            ways_for_change[i] -= ways_for_change[i - lowest]
        else:
            lowest = find_lowest()  # O(n)
    else:
        return coins


assert coins_in_use([1, 0, 1, 1, 2]) == [2, 3, 4]

assert coins_in_use([1, 1, 1, 1, 1]) == [1]
assert coins_in_use([1, 1, 2, 2, 4]) == [1, 2, 4]

assert coins_in_use([1, 1, 2, 3, 5, 7]) == [1, 2, 3, 4, 5]
assert coins_in_use([1, 1, 2, 3, 5]) == [1, 2, 3, 4]
assert coins_in_use([1, 1, 2, 3]) == [1, 2, 3]
