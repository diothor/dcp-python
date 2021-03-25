from itertools import product


def neighbours(y: int, x: int, nrow: int, ncol: int) -> list:
    res = []
    if x > 0:  # left
        res.append((y, x - 1))
    if y > 0:  # top
        res.append((y - 1, x))
    if x < ncol - 1:  # rigth
        res.append((y, x + 1))
    if y < nrow - 1:  # bottom
        res.append((y + 1, x))
    return res


def dfs(board: list, nrow: int, ncol: int, word: str, nletter: int, iletter: int, visited: set, y: int, x: int):
    if (y, x) in visited:
        return False
    else:
        visited.add((y, x))

    if board[y][x] != word[iletter]:
        return False
    elif iletter == nletter - 1:
        return True

    nbrs = neighbours(y, x, nrow, ncol)
    for ny, nx in nbrs:
        if dfs(board, nrow, ncol, word, nletter, iletter + 1, visited, ny, nx):
            return True
    else:
        return False


# O(n^2) where n is number of letters in the board
def exists(board: list, word: str) -> bool:
    nrow, ncol = len(board), len(board[0])
    for y, x in product(range(nrow), range(ncol)):  # O(n) where n is number of letters in the board
        if dfs(board, nrow, ncol, word, len(word), 0, set(), y, x):  # O(n) where n is number of letters in the board
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
