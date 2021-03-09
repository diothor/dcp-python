# O(n^2)
def intersections(p_points: list, q_points: list) -> int:
    intersection_count = 0
    for i in range(len(p_points)):
        pi = p_points[i]
        qi = q_points[i]
        for j in range(i + 1, len(p_points)):
            pj = p_points[j]
            qj = q_points[j]
            pdif = pi - pj
            qdif = qi - qj
            if pdif * qdif < 0:
                intersection_count += 1
    else:
        return intersection_count


assert intersections([2, 15], [4, 10]) == 0
assert intersections([5, 6, 8], [3, 2, 1]) == 3
assert intersections([2, 4, 6, 7, 8, 9, 10], [2, 5, 4, 6, 7, 8, 1]) == 7
assert intersections([i for i in range(4)], [i for i in range(4, -1, -1)]) == 6
