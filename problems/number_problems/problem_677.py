from itertools import islice


# O(nloglogn)
def primes(limit: int) -> list:
    is_prime = [True] * limit

    num = 2
    while num * num <= limit:
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


def prime_generator():
    not_primes = {}
    next_prime = 2
    while True:
        not_primes[next_prime * next_prime] = next_prime
        yield next_prime
        next_prime += 1
        while next_prime in not_primes.keys():
            prime_base = not_primes[next_prime]
            next_multiple = next_prime + prime_base
            if next_multiple in not_primes:
                next_multiple += prime_base
            not_primes[next_multiple] = prime_base
            del (not_primes[next_prime])
            next_prime += 1


prime_nums = list(islice(prime_generator(), 10))
assert prime_nums == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
