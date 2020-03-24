def dfs(graph: list, root: int) -> list:
    vnum = len(graph)
    visited = [False] * vnum

    traversal_path = []
    to_visit = [root]
    while to_visit:
        neighbour = to_visit.pop(0)
        traversal_path.append(neighbour)
        visited[neighbour] = True
        [to_visit.insert(0, v) for v in reversed(graph[neighbour]) if not visited[v]]
    return traversal_path


def dfs_recursive(graph: list, root: int) -> list:
    traversal_path = []
    visited = [False] * len(graph)
    return __dfs_recursive(graph, root, visited, traversal_path)


def __dfs_recursive(graph, vertice, visited, path):
    path.append(vertice)
    visited[vertice] = True
    for n in graph[vertice]:
        if not visited[n]:
            __dfs_recursive(graph, n, visited, path)
    return path


graph = [
    [0, 1, 2],
    [1, 2],
    [0, 2, 3],
    [3]
]
print(dfs(graph, 2))
print(dfs_recursive(graph, 2))
