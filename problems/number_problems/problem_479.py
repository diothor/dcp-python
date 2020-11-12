from typing import List, Any, Set


# O(n*n!)
def permutations(elements_to_permute: List[Any], element_used: Set[Any] = None) -> List[List[Any]]:
    if element_used is None:
        element_used = set()

    if len(elements_to_permute) == len(element_used):
        # O(n!) in total for all runs
        return [[]]

    generated_permutations = []
    for num in elements_to_permute:
        if num in element_used:
            continue
        element_used.add(num)
        for p in permutations(elements_to_permute, element_used):
            # O(n*n!) in total for all runs
            p.append(num)                       # O(1)
            generated_permutations.append(p)    # O(1)
        element_used.remove(num)
    else:
        generated_permutations.sort()
        return generated_permutations


assert permutations([1, 2, 3]) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert permutations([1, 2, 3, 4]) == sorted([
    [1, 2, 3, 4], [2, 1, 3, 4], [3, 1, 2, 4], [1, 3, 2, 4], [2, 3, 1, 4], [3, 2, 1, 4], [4, 2, 1, 3], [2, 4, 1, 3], [1, 4, 2, 3], [4, 1, 2, 3], [2, 1, 4, 3], [1, 2, 4, 3],
    [1, 3, 4, 2], [3, 1, 4, 2], [4, 1, 3, 2], [1, 4, 3, 2], [3, 4, 1, 2], [4, 3, 1, 2], [4, 3, 2, 1], [3, 4, 2, 1], [2, 4, 3, 1], [4, 2, 3, 1], [3, 2, 4, 1], [2, 3, 4, 1]
])
assert permutations(['A', 'B']) == [['A', 'B'], ['B', 'A']]

# the algorithm suscks for duplicates - mostly cause of line #16
assert permutations(['A', 'A']) == []
