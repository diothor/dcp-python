from math import sqrt


# O(n*loglogn)
def eratosthenes_sieve(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for num in range(2, int(sqrt(limit) + 1)):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    else:
        return [num for num, prime in enumerate(is_prime) if prime]


# O(n*loglogn)
def prime_summands(n: int) -> (int, int):
    if n < 3:
        raise ValueError(f'Input number {n} is beyond supported range. Must be greater than 2.')

    primes = eratosthenes_sieve(n)
    for p1 in primes:
        p2 = n - p1
        if p2 in primes:
            return p1, p2
    else:
        raise Exception('Wrong Algorithm')


assert prime_summands(4) == (2, 2)
assert prime_summands(5) == (2, 3)

assert prime_summands(74) == (3, 71)
assert prime_summands(1024) == (3, 1021)
assert prime_summands(66) == (5, 61)
assert prime_summands(9990) == (17, 9973)

try:
    prime_summands(2)
    assert False
except ValueError as e:
    assert True
