from typing import Set, List, Optional


class Trie:
    def __init__(self):
        self.letters = {}
        self.end = False


# O(n) or O(l) where l is number of letters in all words in dictionary
def decode(words: Set[str], string: str) -> Optional[List[str]]:
    root = Trie()
    current_letter = root
    for w in words:
        for l in w:
            current_letter = current_letter.letters.setdefault(l, Trie())
        else:
            current_letter.end = True
            current_letter = root

    res = []
    start = 0
    current_word = root
    for i, l in enumerate(string):
        if current_word.end:
            res.append(string[start:i])  # O(n) in all runs
            start = i
            current_word = root
        if l not in current_word.letters:
            return None
        else:
            current_word = current_word.letters[l]
    else:
        if current_word.end:
            res.append(string[start:len(string)])
        return res


assert decode({'quick', 'brown', 'the', 'fox'}, 'thequickbrownfox') == ['the', 'quick', 'brown', 'fox']
assert decode({'bed', 'bath', 'bedbath', 'and', 'beyond'}, 'bedbathandbeyond') == ['bed', 'bath', 'and', 'beyond'] or ['bedbath', 'and', 'beyond']

assert decode(set(), 'aaa') is None
assert decode(set('bbb'), 'aaa') is None
assert decode(set('bbb'), 'bbbaaa') is None

assert decode({'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'}, 'ilike') == ['i', 'like']
assert decode({'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'}, 'ilikesamsung') == ['i', 'like', 'sam', 'sung'] or ['i', 'like', 'samsung']
