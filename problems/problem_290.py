from itertools import zip_longest

types = {'R', 'G', 'B'}


def merge_quxes(quxes: list) -> list:
    merged = []
    for a, b in zip_longest(quxes[::2], quxes[1::2]):
        if b is None:
            merged += a
        elif a == b:
            merged += a, b
        else:
            merged += types - {a, b}

    return merged if merged == quxes else merge_quxes(merged)


assert merge_quxes(['G']) == ['G']
assert merge_quxes(['B', 'B']) == ['B', 'B']
assert merge_quxes(['R', 'G', 'B', 'G', 'B']) == ['R']
