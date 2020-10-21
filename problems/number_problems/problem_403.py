from random import randint
from collections import Counter

count = 0


def rand5() -> int:
    global count
    count += 1
    return randint(1, 5)


def rand7() -> int:
    to_mod = 5 * rand5() - rand5() + 1
    return to_mod % 7 + 1 if to_mod < 22 else rand7()


rounds_per_num = 100_000
rounds_total = 7 * rounds_per_num

random_nums = [rand7() for _ in range(rounds_total)]
nums_distr = Counter(random_nums)

# log number distribution and rand5() efficiency
print(sorted(nums_distr.items()), count / rounds_total)

# validate that random numbers has uniform distribution
assert all(map(lambda qantity: qantity - rounds_per_num < 0.01 * rounds_per_num, nums_distr.values()))

# validate that rand5() is issued as little times as possible
assert count / rounds_total < 2.4
