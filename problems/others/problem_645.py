from typing import List


def track_word(word: str, w_size: int, iletter: int, matrix: List[List[str]], x: int, y: int, horizontal: bool) -> bool:
    try:
        if word[iletter] != matrix[y][x]:
            return False
        elif iletter == w_size - 1:
            return True
        elif horizontal:
            return track_word(word, w_size, iletter + 1, matrix, x + 1, y, horizontal)
        else:
            return track_word(word, w_size, iletter + 1, matrix, x, y + 1, horizontal)
    except IndexError:
        return False


# O(R*C*L) where R is number of rows in matrix, C is number of columns in matrix and W is number of letters in word
def word_in_matrix(word: str, matrix: List[List[str]]) -> bool:
    word_len = len(word)
    col_len = len(matrix)
    if not col_len:
        return False
    row_len = len(matrix[0])
    if not row_len:
        return False

    for y in range(col_len):
        for x in range(row_len - word_len + 1):
            if track_word(word, word_len, 0, matrix, x, y, True):
                return True

    for x in range(row_len):
        for y in range(col_len - word_len + 1):
            if track_word(word, word_len, 0, matrix, x, y, False):
                return True

    return False


assert word_in_matrix('FAM', [['F', 'F', 'A', 'M']]) is True

assert word_in_matrix('A', [['A']]) is True
assert word_in_matrix('B', [['A']]) is False

assert word_in_matrix('B', [['A', 'B']]) is True
assert word_in_matrix('B', [['A'], ['B']]) is True

assert word_in_matrix('AB', [['A', 'B']]) is True
assert word_in_matrix('AB', [['A'], ['B']]) is True
assert word_in_matrix('BA', [['A', 'B']]) is False
assert word_in_matrix('BA', [['A'], ['B']]) is False

assert word_in_matrix('A', []) is False
assert word_in_matrix('A', [[]]) is False

test_matrix = [['F', 'A', 'C', 'I'],
               ['O', 'B', 'Q', 'P'],
               ['A', 'N', 'O', 'B'],
               ['M', 'A', 'S', 'S']]

# Acceptance cases
assert word_in_matrix('FOAM', test_matrix) is True
assert word_in_matrix('MASS', test_matrix) is True

# Additional cases - positive
assert word_in_matrix('ABNA', test_matrix) is True
assert word_in_matrix('BS', test_matrix) is True

# Additional cases - negative
assert word_in_matrix('IPBSS', test_matrix) is False
assert word_in_matrix('ANOBS', test_matrix) is False
assert word_in_matrix('FOAN', test_matrix) is False
assert word_in_matrix('OBN', test_matrix) is False
assert word_in_matrix('ON', test_matrix) is False
assert word_in_matrix('NB', test_matrix) is False

worst_case = [
    ['A', 'A', 'A'],
    ['A', 'A', 'A'],
    ['A', 'B', 'C'],
]
assert word_in_matrix('AC', worst_case) is True
assert word_in_matrix('AD', worst_case) is False
assert word_in_matrix('D', worst_case) is False
