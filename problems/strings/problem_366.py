from typing import Union


# n is number of all letters in a word equal to len(w)
# k is number of unique letters in a word eqial to len({l for l in w})
# O(n) + O(n) * O(klogk) ~= O(nklogk)
def rearrange(word: str) -> Union[str, None]:
    letters = {}
    for l in word:  # O(n)
        letters.setdefault(l, 0)
        letters[l] += 1

    max_key = max(letters, key=letters.get)
    if letters[max_key] > len(word) - letters[max_key] + 1:
        return None

    res = ''
    last = ''
    # O(n) * O(klogk)
    while letters:  # O(n)
        letters_frequency = sorted(letters.items(), key=lambda i: i[1])  # O(klogk)
        next_letter = letters_frequency[-1][0] if len(letters_frequency) < 2 or last != letters_frequency[-1][0] else letters_frequency[-2][0]
        res += next_letter
        last = next_letter
        letters[next_letter] -= 1
        if letters[next_letter] < 1:
            del(letters[next_letter])
    else:
        return res


assert rearrange('yyz') == 'yzy'
assert rearrange('yyy') is None

assert rearrange('aaabc') == 'acaba'
assert rearrange('aaabb') == 'ababa'
assert rearrange('aaaabc') is None
assert rearrange('aa') is None
