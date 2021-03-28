from typing import Dict, List, Tuple, Union
import heapq


# V is number of vertices
# E is number of edges
# O(E*logV)
def propagation_time(edges: List[Tuple[int, int, int]], nvertices: int, root: int) -> int:
    graph: Dict[int, List[Tuple[int, int]]] = {v: [] for v in range(nvertices)}  # O(V)
    for src, dst, time in edges:  # O(E)
        graph[src].append((dst, time))  # O(1)

    min_time_from_root: List[Union[float, int]] = [float('inf')] * nvertices

    vertice_to_visit = [(0, root)]
    while vertice_to_visit:  # O(E+1)
        path_time, vertex = heapq.heappop(vertice_to_visit)  # O(1)
        if path_time < min_time_from_root[vertex]:
            min_time_from_root[vertex] = path_time
            for nbr, vertex_nbr_time in graph[vertex]:  # O(E) in all runs totally
                heapq.heappush(vertice_to_visit, (path_time + vertex_nbr_time, nbr))  # O(logV)
    else:
        return max(min_time_from_root)  # O(V)


test_edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
assert propagation_time(test_edges, 6, 0) == 9
