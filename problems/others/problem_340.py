from math import sqrt
from operator import itemgetter
from typing import Tuple, Set, List, Dict


class Point:
    def __init__(self, coordinates: Tuple[int, int]):
        self.x, self.y = coordinates

    def __repr__(self):
        return f'P(x: {self.x}, y: {self.y})'

    def to_tuple(self):
        return self.x, self.y


# O(1)
def __dist(p1: Point, p2: Point) -> float:
    dist_square = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
    return round(sqrt(dist_square), 3)


# O(n^2) where n is number of points to check
def __closest_pair_naive(points: List[Point], n: int) -> Dict[float, Set[Point]]:
    closest_points = set()
    min_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            new_dist = __dist(points[i], points[j])
            if new_dist < min_dist:
                min_dist = new_dist
                closest_points = {points[i], points[j]}
    else:
        return {min_dist: closest_points}


# O(n/2) ~= O(n)
def __border_points(points: List[Point], median: int, border_range: float) -> list:
    border_points = [points[median]]
    median_point = points[median]
    left, right = median - 1, median + 1
    while left >= 0 or right < len(points):
        if left >= 0 and abs(median_point.x - points[left].x) < border_range:
            border_points.append(points[left])

        if right < len(points) and abs(median_point.x - points[right].x) < border_range:
            border_points.append(points[right])

        left -= 1
        right += 1
    else:
        return border_points


# O(nlogn)
def __closest_pair_border(points: List[Point], border_range: float) -> Dict[float, Set[Point]]:
    points.sort(key=lambda p: p.y)  # O(nlogn)
    border_pair = set()
    dist_border = border_range
    for index_a, point_a in enumerate(points):  # O(n)
        for point_b in points[index_a + 1:index_a + 8]:  # O(7) ~= O(1)
            if abs(point_a.y - point_b.y) > dist_border:
                break
            new_dist = __dist(point_a, point_b)
            if new_dist < dist_border:
                dist_border = new_dist
                border_pair = {point_a, point_b}
    else:
        return {dist_border if border_pair else float('inf'): border_pair}


# it returns distance beetween two closest points and the points
# O(nlogn)
def __closest_pair_recur(points: List[Point]) -> Dict[float, Set[Point]]:
    # conquer - O(1)
    size = len(points)
    if size < 4:
        # O(1) cause there are 3 or less points for the naive (or brute force) method. The method calculates and compares distances of just 3 pairs of points -> C(3, 2).
        return __closest_pair_naive(points, size)

    # divide - 2*O(logn) ~= O(logn)
    median = size // 2
    dist_with_pair = {}
    dist_with_pair.update(__closest_pair_recur(points[:median]))
    dist_with_pair.update(__closest_pair_recur(points[median:]))

    # merge - O(n) + O(nlogm) ~= O(nlogn)
    dist_min = min(dist_with_pair)
    border_points = __border_points(points, median, dist_min)  # O(n)
    dist_with_pair.update(__closest_pair_border(border_points, dist_min))  # O(nlogn)

    dist_min = min(dist_with_pair)
    return {dist_min: dist_with_pair[dist_min]}


# 2*O(nlogn) ~= O(nlogn)
def closest_pair(*points) -> Set[Tuple[int, int]]:
    sorted_pts = [Point(p) for p in sorted(points, key=itemgetter(0, 1))]  # O(nlogn)
    closest_pts = __closest_pair_recur(sorted_pts).popitem()[1]  # O(nlogn)
    return {p for p in map(Point.to_tuple, closest_pts)}


assert closest_pair((1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)) == {(-1, -1), (1, 1)}
assert closest_pair((2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)) == {(2, 3), (3, 4)}
assert closest_pair((1, 1), (-1, -1), (6, 1), (-1, -6), (-4, -3), (2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)) == {(5, 1), (6, 1)}
