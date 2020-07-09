# O(n^2) where n is number of points
def closest(*points) -> set:
    res_pair = set()
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            new_dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            if new_dist < min_dist:
                min_dist = new_dist
                res_pair = {p1, p2}
    else:
        return res_pair


assert closest((1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)) == {(-1, -1), (1, 1)}
assert closest((2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)) == {(2, 3), (3, 4)}
