from operator import itemgetter
import sys


def traversal_time(edge_list: list, nodes: int) -> int:
    visited = [False] * (nodes + 1)
    dist = [0] + [sys.maxsize] * nodes
    while not all(visited):
        closest = min([(i, v) for i, v in enumerate(dist) if not visited[i]], key=itemgetter(1))
        visited[closest[0]] = True
        neighbours = [edge for edge in edge_list if edge[0] == closest[0]]
        for _, b, t in neighbours:
            new_dist = closest[1] + t
            if new_dist < dist[b]:
                dist[b] = closest[1] + t
    return max(dist)


edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
time = traversal_time(edges, 5)
assert time == 9, time
