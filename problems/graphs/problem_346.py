def connection(src: str, dst: str, hops: int, flights: list, price: int = 0) -> tuple:
    visited = set()
    parent = {src: None}
    cost = {src: 0}
    to_visit = {src}

    while to_visit:
        city = to_visit.pop()
        if city in visited:
            continue

        visited.add(city)
        nbrs = [(n, p) for c, n, p in flights if c == city]
        for nbr, price in nbrs:
            to_visit.add(nbr)
            new_cost = cost[city] + price
            old_cost = cost.setdefault(nbr, float('inf'))
            if old_cost > new_cost:
                cost[nbr] = new_cost
                parent[nbr] = city

    path = []
    hop = dst
    while hop and hops > -1:
        path.insert(0, hop)
        hop = parent[hop]
        hops -= 1
    return (tuple(path), cost[dst]) if path[0] == src else ((), None)


test_flights = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]

assert connection('JFK', 'LAX', 3, test_flights) == (('JFK', 'ATL', 'ORD', 'LAX'), 440)
assert connection('JFK', 'LAX', 2, test_flights) == ((), None)
