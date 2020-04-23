def with_view(buildings) -> int:
    highest = 0
    count = 0
    for b in reversed(buildings):
        if b > highest:
            highest = b
            count += 1
    return count


assert with_view([3, 7, 8, 3, 6, 1]) == 3
assert with_view([9, 2, 8, 4, 7]) == 3
