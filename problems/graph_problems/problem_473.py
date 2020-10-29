from typing import List


def transpose_graph(adjacency_list: List[List[int]]) -> List[List[int]]:
    tgraph = [[] for _ in range(len(adjacency_list))]
    for row_i in range(len(adjacency_list)):
        for col in adjacency_list[row_i]:
            tgraph[col].append(row_i)
    else:
        return tgraph


to_test = [
    [1, 4, 3],
    [],
    [0],
    [2],
    [1, 3]
]
expected = [
    [2],
    [0, 4],
    [3],
    [0, 4],
    [0]
]
assert transpose_graph(to_test) == expected

to_test = [
    [1],
    [2],
    []
]
expected = [
    [],
    [0],
    [1]
]
assert transpose_graph(to_test) == expected