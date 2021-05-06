from typing import List, Set, Any
from itertools import combinations


# O(n*2^n) where n is number of elements in s
def power_set(s: Set) -> List[Set[Any]]:
    res = [set()]
    for level in range(len(s)):  # O(n)
        res += map(set, combinations(s, level + 1))  # O(2^n) subsets are added to res, each having n elements top
    else:
        return res


# basic cases
assert power_set(set()) == [set()]
assert power_set({'a'}) == [set(), {'a'}]
assert power_set({'a', 'b'}) == [set(), {'a'}, {'b'}, {'a', 'b'}]

# acceptance cases
assert power_set({1, 2, 3}) == [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
assert power_set({1, 2, 3, 4}) == [set(), {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}, {1, 2, 3},
                                   {1, 2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}]
