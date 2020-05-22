from itertools import product


def is_toeplitz(matrix: list) -> bool:
    row_num = len(matrix)
    col_num = len(matrix[0])
    for row, col in product(range(1, row_num), range(1, col_num)):
        if matrix[row][col] != matrix[row - 1][col - 1]:
            return False
    else:
        return True


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
