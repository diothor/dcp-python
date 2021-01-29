def dominos(size: int) -> int:
    if size < 3:
        return size
    else:
        return dominos(size - 1) + dominos(size - 2)


def trominos(size: int) -> int:
    if size < 3:
        return 0
    else:
        return 2 * trominos(size - 1) + 2 * trominos(size - 2) + 2


def tilings(size: int) -> int:
    return dominos(size) + trominos(size)


assert tilings(0) == 0
assert tilings(1) == 1
assert tilings(2) == 2
assert tilings(3) == 5
assert tilings(4) == 11
assert tilings(5) == 26
