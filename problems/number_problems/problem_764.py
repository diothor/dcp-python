from collections import Counter


# O(nlogn)
def largest_number(*args: int) -> int:
    counter = Counter(args)
    num_stings = [str(val) * freq for val, freq in counter.items()]
    max_size = max(map(len, num_stings)) + 1
    num_pairs = {(n * max_size)[:max_size]: n for n in num_stings}
    sorted_nums = map(lambda k: num_pairs[k], sorted(num_pairs, reverse=True))
    return int(''.join(sorted_nums))


# basic test cases
assert largest_number(0) == 0
assert largest_number(41, 42) == 4241
assert largest_number(42, 41) == 4241
assert largest_number(43, 42) == 4342
assert largest_number(42, 43) == 4342

# repeated values
assert largest_number(41, 42, 41) == 424141
assert largest_number(42, 41, 42) == 424241

# acceptance test cases
assert largest_number(10, 7, 76, 415) == 77641510
assert largest_number(1, 34, 3, 98, 9, 76, 45, 4, 12, 121) == 99876454343121211
