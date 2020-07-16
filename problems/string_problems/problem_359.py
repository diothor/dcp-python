from typing import Union
from random import sample
from collections import Counter


def anagram(s) -> str:
    return sample(s, len(s))


# O(n) where n is number of encoded numbers
def decode(s) -> Union[int, None]:
    if not s:
        return None

    num_words = list(map(Counter, ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
    all_letters = Counter(s)

    decoded = 0
    num_int = 0
    while num_int < len(num_words) and all_letters:  # O(n) + O(9)
        num_word = num_words[num_int]
        if all_letters & num_word == num_word:
            all_letters -= num_word
            decoded = 10 * decoded + num_int
        else:
            num_int += 1
    else:
        return None if all_letters else decoded


assert decode('') is None
assert decode('zzzz') is None
assert decode('zzzzone') is None

assert decode('niesevehrtfeev') == 357
assert decode(anagram('oneoneone')) == 111
