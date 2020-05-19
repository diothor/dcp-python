# O(n+k)
def all_together_cost(seats: list) -> int:
    # n - number of seats equal to len(seats)
    n = len(seats)

    # O(n)
    ppl = [i for i, v in enumerate(seats) if v]

    # k - number of people equal to seats.count(1)
    k = len(ppl)
    if k == 0:
        return -1

    middle_person = ppl[k // 2]
    hops = 0

    # O(k/2)
    seat_on_left = middle_person - 1
    for i in range(k // 2 - 1, -1, -1):
        person_on_left = ppl[i]
        hops += seat_on_left - person_on_left
        seat_on_left -= 1

    # O(k/2)
    seat_on_right = middle_person + 1
    for r in range(k // 2 + 1, k):
        person_on_right = ppl[r]
        hops += person_on_right - seat_on_right
        seat_on_right += 1

    return hops


assert all_together_cost([0]) == -1
assert all_together_cost([1]) == 0
assert all_together_cost([1, 1, 0, 1, 1, 1]) == 2
assert all_together_cost([1, 0, 1, 0, 1]) == 2
assert all_together_cost([1, 0, 1, 0, 1, 1]) == 3
assert all_together_cost([1, 1, 0, 1, 0, 1]) == 3
assert all_together_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
