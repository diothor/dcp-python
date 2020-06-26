def adjacent_points(point: tuple, matrix_size: tuple) -> list:
    y, x = point
    max_y, max_x, = matrix_size
    adjacent = []
    if y > 0:
        adjacent.append((y - 1, x))
    if y < max_y - 1:
        adjacent.append((y + 1, x))
    if x > 0:
        adjacent.append((y, x - 1))
    if x < max_x - 1:
        adjacent.append((y, x + 1))
    return adjacent


def get_from_matrix(matrix: list, point: tuple):
    return matrix[point[0]][point[1]]


def set_in_matrix(matrix: list, point: tuple, value):
    matrix[point[0]][point[1]] = value


def path_length(matrix: list, start: tuple, end: tuple) -> int or None:
    # size = (n, m)
    matrix_size = (len(matrix), len(matrix[0]))

    # O(n x m)
    hops = [[float('inf')] * matrix_size[1] for _ in range(matrix_size[0])]
    set_in_matrix(hops, start, 0)

    # O(n x m)
    visited = set()
    to_visit = [start]
    while to_visit:
        current = to_visit.pop()  # O(1)
        if current == end:
            break

        visited.add(current)  # O(1)
        next_hop = get_from_matrix(hops, current) + 1  # O(1)
        for y, x in adjacent_points(current, matrix_size):
            if not matrix[y][x] and (y, x) not in visited:
                hops[y][x] = min(next_hop, hops[y][x])  # O(1)
                to_visit.append((y, x))  # O(1)

    res = get_from_matrix(hops, end)
    return res if res < float('inf') else None


assert path_length([[False, False, False, False],
                    [True, True, False, True],
                    [False, False, False, False],
                    [False, False, False, False]], (3, 0), (0, 0)) == 7

assert path_length([[False, False, False],
                    [True, True, True],
                    [False, False, False]], (0, 0), (2, 2)) is None

from_geeks = [[False, True, False, False, False, False, True, False, False, False],
              [False, True, False, True, False, False, False, True, False, False],
              [False, False, False, True, False, False, True, False, True, False],
              [True, True, True, True, False, True, True, True, True, False],
              [False, False, False, True, False, False, False, True, False, True],
              [False, True, False, False, False, False, True, False, True, True],
              [False, True, True, True, True, True, True, True, True, False],
              [False, True, False, False, False, False, True, False, False, False],
              [False, False, True, True, True, True, False, True, True, False]]
assert path_length(from_geeks, (0, 0), (3, 4)) == 11
