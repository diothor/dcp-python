from typing import List


# O(m*n) where n is length of the 'a' string and n is length of the 'b' string
def edit_distance(a: str, b: str, a_index: int = None, b_index: int = None, memoize: List[List[int]] = None) -> int:
    if a_index is None:
        a_index = len(a) - 1
    if b_index is None:
        b_index = len(b) - 1
    if memoize is None:
        memoize = [[-1 for _ in range(len(b))] for _ in range(len(a))]

    if a_index < 0:
        return b_index + 1  # insert the rest of 2nd string
    if b_index < 0:
        return a_index + 1  # delete the rest of 1st string

    if memoize[a_index][b_index] > -1:
        return memoize[a_index][b_index]

    if a[a_index] == b[b_index]:
        memoize[a_index][b_index] = edit_distance(a, b, a_index - 1, b_index - 1, memoize)  # the same letters, nothing to do, keep going for next letters
    else:
        memoize[a_index][b_index] = 1 + min(
            edit_distance(a, b, a_index - 1, b_index - 1, memoize),  # change letter in the 'a' string
            edit_distance(a, b, a_index, b_index - 1, memoize),  # insert letter in the 'a' string
            edit_distance(a, b, a_index - 1, b_index, memoize)  # delete letter in the 'a' string
        )
    return memoize[a_index][b_index]


assert edit_distance('sitting', 'kitten') == 3
assert edit_distance('kitten', 'sitting') == 3

assert edit_distance('abc', 'cba') == 2
assert edit_distance('abe', 'abcde') == 2

assert edit_distance('ab', 'x') == 2
assert edit_distance('abc', 'xyzz') == 4
assert edit_distance('abc', 'xyz') == 3

assert edit_distance('geek', 'gesek') == 1
assert edit_distance('sunday', 'saturday') == 3
