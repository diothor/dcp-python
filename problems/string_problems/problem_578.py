# O(n)
def isomorphic(map_from: str, map_to: str) -> bool:
    if len(map_from) != len(map_to):
        return False

    mapping = {}
    for i, l in enumerate(map_from):
        if l not in mapping:
            mapping[l] = map_to[i]
        elif mapping[l] != map_to[i]:
            return False
    else:
        return True


assert isomorphic('abc', 'bcd') is True
assert isomorphic('foo', 'bar') is False

assert isomorphic('abc', 'bc') is False
assert isomorphic('abb', 'bc') is False
assert isomorphic('abc', 'bcde') is False
