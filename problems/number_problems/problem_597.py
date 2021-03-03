# O(n^2)
def has_pythagorean_triplet(*nums: int) -> bool:
    sqrts = {i ** 2 for i in nums}  # O(n)
    for a, b in [(va, vb) for ia, va in enumerate(sqrts) for ib, vb in enumerate(sqrts) if ib > ia]:  # O(n^2)
        if a + b in sqrts:  # O(1)
            return True
    else:
        return False


assert has_pythagorean_triplet(3, 1, 4, 6, 5) is True
assert has_pythagorean_triplet(10, 4, 6, 12, 5) is False
