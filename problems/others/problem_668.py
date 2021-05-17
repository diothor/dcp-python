def same_on_diagonal(x, y, matrix, rows, cols) -> bool:
    val = matrix[y][x]
    x += 1
    y += 1
    while x < cols and y < rows:
        if matrix[y][x] != val:
            return False
        else:
            x += 1
            y += 1
    else:
        return True


# O(n) where n is number of all elements in the matrix
def is_toeplitz(matrix: list) -> bool:
    if not matrix:
        return False
    nrow = len(matrix)
    ncol = len(matrix[0])
    for x in range(ncol - 1):
        if not same_on_diagonal(x, 0, matrix, nrow, ncol):
            return False
    for y in range(1, nrow - 1):
        if not same_on_diagonal(0, y, matrix, nrow, ncol):
            return False
    else:
        return True


assert is_toeplitz([]) is False
assert is_toeplitz(['A']) is True

assert is_toeplitz([
    ['A', 'B'],
    ['B', 'A'],
]) is True

assert is_toeplitz([
    ['A', 'B'],
    ['B', 'C'],
]) is False

assert is_toeplitz([
    ['C', 'B'],
    ['B', 'A'],
]) is False

assert is_toeplitz([
    ['A', 'B', 'C'],
    ['B', 'A', 'B'],
]) is True

assert is_toeplitz([
    ['A', 'B'],
    ['B', 'A'],
    ['C', 'B'],
]) is True

assert is_toeplitz([
    ['A', 'B', 'C'],
    ['B', 'A', 'D'],
]) is False

assert is_toeplitz([
    ['A', 'B'],
    ['B', 'A'],
    ['C', 'D'],
]) is False


assert is_toeplitz([
    [1, 2, 3, 4, 8],
    [5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3],
    [7, 4, 5, 1, 2]
]) is True

assert is_toeplitz([[6, 7, 8],
                    [4, 6, 7],
                    [1, 4, 6]]) is True

assert is_toeplitz([[6, 7, 8, 9],
                    [4, 6, 7, 8],
                    [1, 4, 6, 7],
                    [0, 1, 4, 6],
                    [2, 0, 1, 4]]) is True

assert is_toeplitz([[6, 3, 8],
                    [4, 9, 7],
                    [1, 4, 6]]) is False
