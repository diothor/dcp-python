from collections import defaultdict


def cut_bricks(brick_rows: list) -> int:
    lengths = defaultdict(int)
    best_length = 0
    for row in brick_rows:
        length = 0
        for brick in row[:-1]:
            length += brick
            lengths[length] += 1
            best_length = max(best_length, lengths[length])
    return len(brick_rows) - best_length


assert cut_bricks([]) == 0

cuts = cut_bricks([[3, 5, 1, 1],
                   [2, 3, 3, 2],
                   [5, 5],
                   [4, 4, 2],
                   [1, 3, 3, 3],
                   [1, 1, 6, 1, 1]])
assert cuts == 2, cuts

cuts = cut_bricks([[1, 2, 2, 1],
                   [3, 1, 2],
                   [1, 3, 2],
                   [2, 4],
                   [3, 1, 2],
                   [1, 3, 1, 1]])
assert cuts == 2, cuts
