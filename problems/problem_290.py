types = {'R', 'G', 'B'}


def merge_quxes(quxes: list) -> int:
    size = len(quxes)
    colors = {k: 0 for k in 'RGB'}
    for q in quxes:
        colors[q] += 1

    if max(colors.values()) == size:
        return size

    parity = [c % 2 for c in colors.values()]
    if len(set(parity)) == 1:
        return 2
    else:
        return 1


assert merge_quxes(['G']) == 1
assert merge_quxes(['B', 'B', 'B']) == 3
assert merge_quxes(['R', 'G', 'B', 'G', 'B']) == 1
assert merge_quxes(['R', 'R', 'R', 'B', 'B', 'B', 'G', 'G', 'G']) == 2
assert merge_quxes(['R', 'G', 'R', 'G', 'B', 'B']) == 2
