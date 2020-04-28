def evacuate(people: list, boat_size: int) -> int:
    boats = 0
    people.sort()  # O(nlogn)
    if len(people) and people[-1] > boat_size:
        raise ValueError(f'Person can not fit in a boat. Weight: {people[-1]}; Boat size: {boat_size}')

    lean = 0
    heavy = len(people) - 1
    while lean <= heavy:  # O(n)
        weight = people[lean] + people[heavy]
        if weight > boat_size:
            boats += 1
            heavy -= 1
        else:
            boats += 1
            heavy -= 1
            lean += 1
    return boats


assert evacuate([], 0) == 0
assert evacuate([60], 100) == 1
assert evacuate([30, 150, 170, 50], 200) == 2
assert evacuate([100, 200, 150, 80], 200) == 3
assert evacuate([150, 150, 150, 150, 30], 200) == 4

try:
    assert evacuate([60], 50) == 1
    raise AssertionError
except ValueError as e:
    pass
