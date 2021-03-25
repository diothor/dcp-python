from itertools import product


def neighbours(size_y, size_x, y, x) -> list:
    res = []
    if x > 0:  # left
        res.append((y, x - 1))
    if y > 0:  # top
        res.append((y - 1, x))
    if x < size_x - 1:  # rigth
        res.append((y, x + 1))
    if y < size_y - 1:  # bottom
        res.append((y + 1, x))
    return res


def dfs(board, size_y, size_x, word, size_w, iletter, visited: set, y, x):
    if (y, x) in visited:
        return False
    else:
        visited.add((y, x))

    if board[y][x] != word[iletter]:
        return False
    elif iletter == size_w - 1:
        return True

    nbrs = neighbours(size_y, size_x, y, x)
    for ny, nx in nbrs:
        if dfs(board, size_y, size_x, word, size_w, iletter + 1, visited, ny, nx):
            return True
    else:
        return False


def exists(board: list, word: str) -> bool:
    size_y, size_x = len(board), len(board[0])
    for y, x in product(range(size_y), range(size_x)):  # O(n) where n is number of letters in the board
        if dfs(board, size_y, size_x, word, len(word), 0, set(), y, x):
            return True
    else:
        return False


test_board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

assert exists(test_board, 'ABCCED') is True
assert exists(test_board, 'SEE') is True
assert exists(test_board, 'ABCB') is False

assert exists(test_board, 'GBFC') is False
assert exists(test_board, 'ABFDA') is True
