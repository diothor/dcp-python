def next_to_travers(cell: dict, matrix: list, visited: list):
    cols, rows = len(matrix[0]), len(matrix)
    x, y = cell.values()
    if y == rows:
        return None
    elif visited[y][x] or matrix[y][x] != '.':
        next_x, next_y = (x + 1, y) if x < cols - 1 else (0, y + 1)
        return next_to_travers({'x': next_x, 'y': next_y}, matrix, visited)
    else:
        return cell


def mark_visited(cell: dict, visited: list) -> dict:
    visited[cell['y']][cell['x']] = True
    return cell


def neighbours(cell: dict, matrix: list, visited: list) -> list:
    cols, rows = len(matrix[0]), len(matrix)
    x, y = cell.values()

    if matrix[y][x] != '.':
        return []

    nbrs = []
    if x > 0:  # add left
        nbrs.append({'x': x - 1, 'y': y})
    if y > 0:  # add top
        nbrs.append({'x': x, 'y': y - 1})
    if x < cols - 1:  # add right
        nbrs.append({'x': x + 1, 'y': y})
    if y < rows - 1:  # add bottom
        nbrs.append({'x': x, 'y': y + 1})

    nbrs = filter(lambda c: visited[c['y']][c['x']] is False, nbrs)
    return list(nbrs)


def regions(matrix: list) -> int:
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    region_count = 0
    to_traverse = next_to_travers({'x': 0, 'y': 0}, matrix, visited)
    complexity = 0
    while to_traverse:
        to_visit = [to_traverse]
        while to_visit:
            cell = to_visit.pop()
            if visited[cell['y']][cell['x']]:
                continue
            mark_visited(cell, visited)
            complexity += 1
            nbrs = neighbours(cell, matrix, visited)
            to_visit += nbrs
        else:
            region_count += 1
        to_traverse = next_to_travers(to_traverse, matrix, visited)

    print(complexity, f'{len(matrix[0])}x{len(matrix)}')
    return region_count


test_matrix = [
    [c for c in '\\..../'],
    [c for c in '.\\../.'],
    [c for c in '..\\/..'],
]
assert regions(test_matrix) == 3

test_matrix = [
    [c for c in './..\\.'],
    [c for c in '/....\\'],
    [c for c in '\\..../'],
    [c for c in '.\\../.'],
    [c for c in '..\\/..'],
]
assert regions(test_matrix) == 5
