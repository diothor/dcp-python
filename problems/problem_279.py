def count_groups(friends: list) -> int:
    groups = 0
    visited = [0] * len(friends)

    while 0 in visited:
        groups += 1
        to_visit = [visited.index(0)]
        while to_visit:
            # .pop() == depth-first; .pop(0) == breadth-first;
            person = to_visit.pop()
            if visited[person] == 1:
                continue
            visited[person] = 1
            to_visit += friends[person]

    return groups
