from typing import Union
import heapq
from collections import Counter


# O(n) + O(n) + O(n*2logn) ~= O(nlogn) where n is number of all characters in `s` and is equal to len(s)
def the_same_not_adjacent(s: str) -> Union[str, None]:
    characters = Counter(s)  # O(n)
    characters = [[-f, ch] for ch, f in characters.items()]  # O(n)
    heapq.heapify(characters)  # O(n)

    last_letter = [0, '']
    res = ''
    # O(n*2logn)
    while characters:  # O(n)
        next_letter = heapq.heappop(characters)  # O(logn)
        res += next_letter[1]
        next_letter[0] += 1
        if last_letter[0] < 0:
            heapq.heappush(characters, last_letter)  # O(logn)
        last_letter = next_letter
    else:
        return res if len(res) == len(s) else None


assert the_same_not_adjacent('yyz') == 'yzy'
assert the_same_not_adjacent('yyy') is None

assert the_same_not_adjacent('aaabc') == 'abaca'
assert the_same_not_adjacent('aaabb') == 'ababa'
assert the_same_not_adjacent('aaaabc') is None
assert the_same_not_adjacent('aa') is None

assert the_same_not_adjacent('zzzzaabb') == 'zazbzabz'
assert the_same_not_adjacent('') == ''

assert the_same_not_adjacent('abcdef') == 'abcdef'
assert the_same_not_adjacent('fedcba') == 'abcdef'
