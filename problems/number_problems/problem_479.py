from typing import Union, List, Any


# O(n*n!)
def permutations(elements_to_permute: List[Any], current_permutation: Union[List[Any], None] = None):
    if current_permutation is None:
        current_permutation = []

    if not elements_to_permute:
        return [current_permutation]

    generated_permutations = []
    for num in elements_to_permute:  # n * (n - 1) * (n - 2) * ... * 1 = n! => O(n!)
        next_permutation = current_permutation + [num]  # O(n)
        remaining_nums = [i for i in elements_to_permute if i != num]  # O(n)
        generated_permutations += permutations(remaining_nums, next_permutation)
    else:
        return generated_permutations


assert permutations([1, 2, 3]) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert permutations([1, 2, 3, 4]) == sorted([
    [1, 2, 3, 4], [2, 1, 3, 4], [3, 1, 2, 4], [1, 3, 2, 4], [2, 3, 1, 4], [3, 2, 1, 4], [4, 2, 1, 3], [2, 4, 1, 3], [1, 4, 2, 3], [4, 1, 2, 3], [2, 1, 4, 3], [1, 2, 4, 3],
    [1, 3, 4, 2], [3, 1, 4, 2], [4, 1, 3, 2], [1, 4, 3, 2], [3, 4, 1, 2], [4, 3, 1, 2], [4, 3, 2, 1], [3, 4, 2, 1], [2, 4, 3, 1], [4, 2, 3, 1], [3, 2, 4, 1], [2, 3, 4, 1]
])
assert permutations(['A', 'B']) == [['A', 'B'], ['B', 'A']]

# the algorithm suscks for duplicates - mostly cause of line #15
assert permutations(['A', 'A']) == [['A'], ['A']]
