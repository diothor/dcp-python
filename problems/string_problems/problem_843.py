from typing import List


# O(n*k)
def find_indices(text: str, pattern: str) -> List[int]:
    n = len(text)
    k = len(pattern)
    indices = []
    for i in range(n - k + 1):
        sub_string = text[i:i + k]
        if pattern == sub_string:
            indices.append(i)
    else:
        return indices


assert find_indices("abc", "bc") == [1]
assert find_indices("ababa", "aba") == [0, 2]
assert find_indices("aaaa", "aa") == [0, 1, 2]


assert find_indices("a", "ab") == []
assert find_indices("abc", "ac") == []

# Acceptance case
assert find_indices('abracadabra', 'abr') == [0, 7]
assert find_indices('GeeksforGeeks', 'Geeks') == [0, 8]
