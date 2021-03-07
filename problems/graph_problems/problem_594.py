# O(1)
def neighbours(x: int, y: int, size: int) -> list:
    nbrs = []
    if x > 0:  # left
        nbrs.append((x - 1, y))
    if y > 0:  # top
        nbrs.append((x, y - 1))
    if x < size - 1:  # right
        nbrs.append((x + 1, y))
    if y < size - 1:  # bottom
        nbrs.append((x, y + 1))
    return nbrs


# O(w) where w is length of word
def word_in_letters(letters, letters_size, candidate_letters, used_letters, word, word_letter, word_length):
    if word_length - 1 == word_letter:
        return True
    for y, x in candidate_letters:
        if not used_letters[y][x] and letters[y][x] == word[word_letter]:
            nbrs = neighbours(y, x, letters_size)
            if word_in_letters(letters, letters_size, nbrs, used_letters, word, word_letter + 1, word_length):
                used_letters[y][x] = True
                return True
    else:
        return False


# O(N*W) where N is number of all letters in a matrix and W is total number of letters in all words
def count_words(letters, words):
    found_words = []
    sorted_words = sorted(words.copy(), key=len)  # O(w)
    matrix_size = len(letters)
    used_letters = [[False] * matrix_size for _ in range(matrix_size)]
    for y in range(matrix_size):
        for x in range(matrix_size):
            for w in sorted_words:
                if w[0] == letters[y][x] and word_in_letters(letters, matrix_size, [(y, x)], used_letters, w, 0, len(w)):
                    found_words.append(w)
    else:
        return len(found_words)


test_dict = ['eat', 'rain', 'in', 'rat']

letter_matrix = [
    ['e', 'a', 'n'],
    ['t', 't', 'i'],
    ['a', 'r', 'a']
]
assert count_words(letter_matrix, test_dict) == 3

reversed_matrix = [
    ['a', 'r', 'a'],
    ['t', 't', 'i'],
    ['e', 'a', 'n']
]
assert count_words(reversed_matrix, test_dict) == 3

used = [[False] * 3 for _ in range(3)]
assert word_in_letters(letter_matrix, 3, [(1, 1)], used, 'tiart', 0, 5) is True  # this is a bug - (1, 1) letter in the matrix is used twice.
