from itertools import zip_longest


def all_together_cost(seats: list) -> int:
    # n - number of seats equal to len(seats)
    n = len(seats)

    ones_out = {i for i in range(n) if seats[i] == 1}  # O(n)
    # k - number of people equal to seats.count(1)
    k = len(ones_out)

    zeros_in = set()
    for i in range(k):  # O(k)
        if seats[i] == 1:
            ones_out.remove(i)
        else:
            zeros_in.add(i)

    # O(n-k) * O(k) ~= O(n*k)
    hops = float('inf')
    for i in range(k, n):  # O(n-k)
        hops = min(hops, sum([abs(a - b) for a, b in zip_longest(zeros_in, ones_out, fillvalue=0)]))  # O(k)

        if seats[i-k] == 0:
            zeros_in.remove(i-k)  # O(1)
        else:
            ones_out.add(i-k)  # O(1)

        if seats[i] == 0:
            zeros_in.add(i)  # O(1)
        else:
            ones_out.remove(i)  # O(1)
    return hops


assert all_together_cost([1, 0, 1, 0, 1]) == 2
assert all_together_cost([1, 0, 1, 0, 1, 1]) == 3
assert all_together_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
