# O(n)
def josephus(n: int, k: int) -> int:
    if n == 1:
        return 1

    survivor = (josephus(n-1, k) + k)
    if survivor % n == 0:
        return n
    else:
        return survivor % n


assert josephus(3, 2) == 3
assert josephus(5, 2) == 3
assert josephus(7, 3) == 4
assert josephus(41, 7) == 31
assert josephus(3, 4) == 2
