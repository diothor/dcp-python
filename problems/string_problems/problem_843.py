from typing import List


# O(n*k)
def start_indices(text: str, pattern: str) -> List[int]:
    n = len(text)
    k = len(pattern)
    indices = []
    for i in range(n - k + 1):
        sub_string = text[i:i + k]
        if pattern == sub_string:
            indices.append(i)
    else:
        return indices


assert start_indices("abc", "bc") == [1]
assert start_indices("ababa", "aba") == [0, 2]
assert start_indices("aaaa", "aa") == [0, 1, 2]


assert start_indices("a", "ab") == []
assert start_indices("abc", "ac") == []

# Acceptance case
assert start_indices('abracadabra', 'abr') == [0, 7]
assert start_indices('GeeksforGeeks', 'Geeks') == [0, 8]
