def skyline(buildings: list) -> list:
    if len(buildings) == 1:
        return to_edges(buildings[0])

    mid = len(buildings) // 2
    left = skyline(buildings[:mid])
    right = skyline(buildings[mid:])
    return merge(left, right)


def to_edges(b: tuple) -> list:
    left, right, height = b
    return [(left, height), (right, 0)]


def merge(line1: list, line2: list) -> list:
    merged = []
    current_h, h1, h2 = 0, 0, 0
    i1, i2 = 0, 0
    while i1 < len(line1) and i2 < len(line2):
        next_line = None
        if line1[i1][0] < line2[i2][0]:
            h1 = line1[i1][1]
            next_line = line1[i1]
            i1 += 1
        else:
            h2 = line2[i2][1]
            next_line = line2[i2]
            i2 += 1

        prev_h, current_h = current_h, max(h1, h2)
        if prev_h != current_h:
            merged.append((next_line[0], current_h))

    return merged + line1[i1:] + line2[i2:]


assert skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)]) == [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
assert skyline([(1, 5, 11), (2, 7, 6), (3, 9, 13), (12, 16, 7), (14, 25, 3), (19, 22, 18), (23, 29, 13), (24, 28, 4)]) == [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (23, 13), (29, 0)]
