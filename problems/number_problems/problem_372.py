# O(n) where n is number of digits in the given integer
def num_of_diggits(num: int) -> int:
    num //= 10
    return 1 + num_of_diggits(num) if num else 1


assert num_of_diggits(0) == 1
assert num_of_diggits(00) == 1
assert num_of_diggits(12345) == 5
