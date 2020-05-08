from operator import itemgetter


def count_votes(votes: list, top_n=3) -> list:
    voters = set()
    candidates = {}
    for v in votes:
        if v[0] not in voters:
            candidates[v[1]] = candidates.setdefault(v[1], 0) + 1
            voters.add(v[0])
        else:
            print(f'Fraoud: {v[0]} has already voted!')
    return [c for c, v in sorted(candidates.items(), key=itemgetter(1), reverse=True)][:top_n]


test_votes = [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 2),
    (0, 1),
]
assert count_votes(test_votes) == [1, 0, 2]
assert count_votes(test_votes, 2) == [1, 0]
