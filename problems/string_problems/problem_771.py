# O(n)
def mapping_exists(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    mapping = {}
    for map_from, map_to in zip(s1, s2):
        map_kept = mapping.setdefault(map_from, map_to)
        if map_kept != map_to:
            return False
    else:
        return True


# corner cases
assert mapping_exists('', '') is False
assert mapping_exists('a', '') is False

# hardest case
assert mapping_exists('abca', '1231') is True
assert mapping_exists('abca', '1232') is False

# acceptance tests
assert mapping_exists('abc', 'bcd') is True
assert mapping_exists('foo', 'bar') is False
