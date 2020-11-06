from typing import List


def permutations(args: List[any], start: int = 0) -> List[List[any]]:
    if len(args) - start < 3:
        reverse_stop_index = start - 1 if start > 0 else None
        return [args[start:], args[-1:reverse_stop_index:-1]]

    res = []
    for i in range(len(args)):
        new_args = args[:i] + args[i+1:]
        perms = permutations(new_args)
        for p in perms:
            p.insert(0, args[i])
            res.append(p)
    else:
        res.sort()
        return res


assert permutations([1, 2, 3]) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert permutations([1, 2, 3, 4]) == sorted([
    [1, 2, 3, 4], [2, 1, 3, 4], [3, 1, 2, 4], [1, 3, 2, 4], [2, 3, 1, 4], [3, 2, 1, 4], [4, 2, 1, 3], [2, 4, 1, 3], [1, 4, 2, 3], [4, 1, 2, 3], [2, 1, 4, 3], [1, 2, 4, 3],
    [1, 3, 4, 2], [3, 1, 4, 2], [4, 1, 3, 2], [1, 4, 3, 2], [3, 4, 1, 2], [4, 3, 1, 2], [4, 3, 2, 1], [3, 4, 2, 1], [2, 4, 3, 1], [4, 2, 3, 1], [3, 2, 4, 1], [2, 3, 4, 1]
])
assert permutations(['A', 'B']) == [['A', 'B'], ['B', 'A']]

# duplicates - I know it sucks
assert permutations(['A', 'A']) == [['A', 'A'], ['A', 'A']]
