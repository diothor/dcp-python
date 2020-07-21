from typing import Union


# O(n)
def magic_index(*sorted_nums: int) -> Union[int, None]:
    for i, v in enumerate(sorted_nums):
        if i == v:
            return i
    else:
        return None


assert magic_index() is None
assert magic_index(4, 6) is None
assert magic_index(-5, -3, 2, 3) == 2
assert magic_index(-5, -3, 0, 3, 4) == 3
