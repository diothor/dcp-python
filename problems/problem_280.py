# check if there is a cycle in an undirected graph
def has_cycle(adj: list) -> bool:
    visited = [False] * len(adj)
    for n in range(len(adj)):
        if not visited[n] and __dfs_rec(n, None, adj, visited):
            return True
    else:
        return False


def __dfs_rec(node, parent, adjacencies, visited):
    visited[node] = True
    for child in adjacencies[node]:
        if not visited[child]:
            cycle_detected = __dfs_rec(child, node, adjacencies, visited)
            if cycle_detected:
                return True
        elif child is not parent:
            return True
    else:
        return False


with_cycle = [
    [1, 2, 3],
    [0, 2],
    [0, 1],
    [0, 4],
    [3]
]
assert has_cycle(with_cycle) is True

no_cycle = [
    [1, 3],
    [0, 2],
    [1],
    [0, 4],
    [3]
]
assert has_cycle(no_cycle) is False
