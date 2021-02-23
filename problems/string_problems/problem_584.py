from typing import Optional
from collections import Counter
from heapq import heapify, heapreplace, heappop


# O(nlogn)
def rearange(s: str) -> Optional[str]:
    if len(s) < 2:
        return None
    letter_heap = [(-freq, letter) for letter, freq in Counter(s).items()]  # O(n)
    heapify(letter_heap)  # O(n)

    freq_used, letter_used = heappop(letter_heap)  # O(1)
    if freq_used > len(s) // 2 + 1:
        return None
    res = [letter_used]
    freq_used += 1
    while letter_heap:  # O(n)
        if freq_used < 0:
            freq_current, letter_current = heapreplace(letter_heap, (freq_used, letter_used))  # O(logn)
        else:
            freq_current, letter_current = heappop(letter_heap)  # O(logn)
        res.append(letter_current)
        letter_used, freq_used = letter_current, freq_current + 1
    else:
        return None if freq_used < 0 else ''.join(res)


assert rearange('aaabbc') == 'ababac'
assert rearange('aaaabbc') == 'ababaca'
assert rearange('aaaaabbc') is None
assert rearange('aaab') is None

assert rearange('aa') is None
assert rearange('aaaabc') is None
assert rearange('aaabb') == 'ababa'
assert rearange('aaabc') == 'abaca'

assert rearange('bbggggz') == 'gbgbgzg'
assert rearange('a') is None
assert rearange('') is None

assert rearange('abc') == 'abc'
assert rearange('bac') == 'abc'  # not the best, but meets requirements
