from typing import List


def primes(max_num: int) -> List[int]:
    if max_num < 2:
        return list()
    is_prime = [i % 2 != 0 for i in range(max_num + 1)]
    is_prime[0] = is_prime[1] = False
    is_prime[2] = True
    p = 3
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    else:
        return [num for num, prime in enumerate(is_prime) if prime]


def prime_terms(input_sum: int) -> (int, int):
    _primes_list = primes(input_sum)
    _primes_set = set(_primes_list)
    for p in _primes_list:
        if (input_sum - p) in _primes_set:
            return p, input_sum - p
    else:
        return 0, 0


assert prime_terms(4) == (2, 2)
assert prime_terms(74) == (3, 71)
assert prime_terms(1024) == (3, 1021)
assert prime_terms(66) == (5, 61)
assert prime_terms(9990) == (17, 9973)
