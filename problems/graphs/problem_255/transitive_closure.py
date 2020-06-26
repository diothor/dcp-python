import graphs.problem_255.search as search


def transitive_closure(graph: list) -> list:
    # create empty closure with graph_size x graph_size
    graph_size = len(graph)
    my_row = [0] * graph_size
    closure = [my_row.copy() for _ in range(graph_size)]

    for vertice in range(len(graph)):
        reachable = search.dfs(graph, vertice)
        for r in reachable:
            closure[vertice][r] = 1

    return closure
