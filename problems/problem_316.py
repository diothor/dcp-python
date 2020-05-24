def coins_in_use(change_ways: list, coin=1, in_use=None) -> list:
    n = len(change_ways)
    if in_use is None:
        in_use = []

    if coin == n:
        return in_use

    needed = change_ways[coin]
    for used in in_use:
        needed -= change_ways[coin - used]

    if needed:
        in_use.append(coin)
    return coins_in_use(change_ways, coin + 1, in_use)


assert coins_in_use([1, 0, 1, 1, 2]) == [2, 3, 4]
assert coins_in_use([1, 0, 1, 1, 1]) == [2, 3]
