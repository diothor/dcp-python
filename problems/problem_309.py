def all_together_cost(seats: list) -> int:
    # n - number of seats equal to len(seats)
    # k - number of people equal to seats.count(1)
    zeros = []
    ones = []
    # O(n)
    for i in range(len(seats)):  # O(n)
        (ones if seats[i] == 1 else zeros).append(i)  # O(1)

    hops = float('inf')
    # O(n) * (2*O(n) + O(k)) ~= O(n^2)
    for i in range(len(seats) - len(ones) + 1):  # O(n)
        window_start = i
        window_end = i + len(ones) - 1
        zeros_in = list(filter(lambda x: window_start <= x < window_end, zeros))  # O(n)
        ones_out = list(filter(lambda x: x < window_start or x > window_end, ones))  # O(n)
        if len(zeros_in) == len(ones_out):
            hops = min(hops, sum([abs(a - b) for a, b in zip(zeros_in, ones_out)]))  # O(k)
    return hops


assert all_together_cost([1, 0, 1, 0, 1]) == 3
assert all_together_cost([1, 0, 1, 0, 1, 1]) == 3
assert all_together_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
