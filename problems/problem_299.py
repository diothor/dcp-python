import heapq


def min_cost(pipes: dict) -> int:
    parents = {k: None for k in pipes}

    costs = {k: float('inf') for k in pipes}
    costs['plant'] = 0

    next_2_visit = []
    heapq.heappush(next_2_visit, (0, 'plant'))

    # V is number of locations, which is equal to len(pipes).
    # P is number of pipes from a single location. It may be V-1 in full-mesh which is the worst case scenario. It's equal to len(pipes[i]) where 0 < i < len(pipes).
    # E is total number of pipes between all locattions equal to V*P.
    # O(V*(logV + P*logV)) ~= O(V*P*logV) ~= O(ElogV)
    while next_2_visit:  # O(V) - iterating over all locations
        loc_cost, loc = heapq.heappop(next_2_visit)  # O(logV) - extracting next lowest-cost location from min-heap
        if loc_cost > costs[loc]:
            # this makes sure that each location is process once despite it may be added multiple times to heap
            continue
        for nbr, pipe_to_nbr in pipes[loc].items():  # O(P) - iterate over pipes getting out of this location
            nbr_cost = loc_cost + pipe_to_nbr
            if nbr_cost < costs[nbr]:
                costs[nbr] = nbr_cost
                parents[nbr] = loc
                heapq.heappush(next_2_visit, (nbr_cost, nbr))  # O(logV)

    # O(V) - getting through all locations, each exactly once
    total_cost = 0
    while parents:
        loc, parent = parents.popitem()
        total_cost += costs[loc]
        while parent:
            parent = parents.pop(parent, None)

    # total complexity is O(ElogV) + O(V)
    return total_cost


test_pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
assert min_cost(test_pipes) == 16
