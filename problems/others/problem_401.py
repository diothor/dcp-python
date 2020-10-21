from typing import List, Any


# O(n)
def permutation(org: List[Any], perm: List[int]) -> List[Any]:
    res = list()
    for i in perm:
        try:
            res.append(org[i])  # amortized O(1)
        except IndexError:
            pass
    else:
        return res


assert permutation(['a', 'b', 'c'], [2, 1, 0]) == ['c', 'b', 'a']
assert permutation(['a', 'b', 'c'], [2, 0, 1]) == ['c', 'a', 'b']
assert permutation([1], [0]) == [1]

assert permutation([], [7]) == []
assert permutation([1], [1]) == []
assert permutation([1, 2, 3, 4], [0, 2, 1, 4, 3]) == [1, 3, 2, 4]

assert permutation([1, 2], []) == []
assert permutation([1, 2, 3], [1, 0]) == [2, 1]
