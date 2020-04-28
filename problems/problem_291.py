def evacuate(people: list, boat_size: int) -> int:
    boats = 0
    while people:
        weight = people[0]
        if weight > boat_size:
            raise ValueError(f'Person can not fit in a boat. Weight: {weight} Boat size: {boat_size}')
        another = None
        for i in range(1, len(people)):
            print(people[0], people[i])
            new_weight = weight + people[i]
            if weight < new_weight <= boat_size:
                weight = new_weight
                another = i
        boats += 1
        if another is not None:
            del(people[another])
        people = people[1:]
    return boats


assert evacuate([100, 200, 150, 80], 200) == 3
