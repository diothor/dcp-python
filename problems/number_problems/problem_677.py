# O(nloglogn)
def primes(limit: int) -> list:
    is_prime = [True] * limit

    num = 2
    while num * num < limit:
        if is_prime[num]:
            for i in range(num * num, limit, num):
                is_prime[i] = False
        num += 1
    else:
        return [num for num, prime in enumerate(is_prime) if prime if num > 1]


assert primes(0) == []
assert primes(1) == []
assert primes(2) == []
assert primes(3) == [2]
assert primes(4) == [2, 3]

assert primes(10) == [2, 3, 5, 7]
assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
