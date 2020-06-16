def closest(points: list) -> list:
    min_pair = None
    min_dist = float('inf')
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            if dist < min_dist:
                min_dist = dist
                min_pair = [p1, p2]
    else:
        return min_pair


assert closest([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]) == [(-1, -1), (1, 1)]
