# O(n^2)
def has_pythagorean_triplet(*args: int) -> bool:
    sqrs = {num ** 2 for num in args}
    for a, b in [(a, b) for ai, a in enumerate(sqrs) for bi, b in enumerate(sqrs) if ai > bi]:
        if a + b in sqrs:  # O(1) cause sqrs is a set
            return True
    else:
        return False


assert has_pythagorean_triplet(3, 1, 4, 6, 5) is True
assert has_pythagorean_triplet(10, 4, 6, 12, 5) is False
