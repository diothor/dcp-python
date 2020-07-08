# O(n^2) where n is number of points
def closest(*points) -> list:
    res_pair = []
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            new_dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            if new_dist < min_dist:
                min_dist = new_dist
                res_pair = [p1, p2]
    else:
        return sorted(res_pair)


assert closest((1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)) == [(-1, -1), (1, 1)]
