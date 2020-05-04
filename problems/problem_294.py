import heapq


def dijkstra(start: int, vertices_num: int, edges: dict) -> list:
    short_path_tree = [float('inf')] * vertices_num
    short_path_tree[start] = 0

    parent = [-1] * vertices_num

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        closest_vertex = heapq.heappop(heap)[1]
        closest_distance = short_path_tree[closest_vertex]

        neighbours = filter(lambda p: p[0][0] == closest_vertex, edges.items())
        for (start, end), weight in neighbours:
            new_distance = closest_distance + weight
            if new_distance < short_path_tree[end]:
                short_path_tree[end] = new_distance
                parent[end] = start
                heapq.heappush(heap, (weight, end))
    return short_path_tree


def route(altitudes: dict, paths: dict) -> int:
    uphill, downhill = {}, {}
    for (start, end), v in paths.items():
        if altitudes[start] < altitudes[end]:
            uphill[(start, end)] = v
        elif altitudes[start] > altitudes[end]:
            downhill[(end, start)] = v

    up_graph = dijkstra(0, len(altitudes), uphill)
    down_graph = dijkstra(0, len(altitudes), downhill)
    routes_length = [a + b for a, b in zip(down_graph, up_graph)]
    return min(routes_length[1:])


path_cost = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
assert route({0: 5, 1: 25, 2: 15, 3: 20, 4: 10}, path_cost) == 28
assert route({0: 5, 1: 25, 2: 4, 3: 20, 4: 10}, path_cost) == 30
