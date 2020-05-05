def longest_of_two(elements: list) -> int:
    longest = 0
    counter = 0
    the_two_values = []
    previous = None
    last_change = 0

    for i, e in enumerate(elements):
        if len(the_two_values) < 2:
            the_two_values.append(e)
        elif e not in the_two_values:
            longest = max(longest, counter)
            counter = i - last_change
            the_two_values = [previous, e]
        counter += 1
        last_change = i if e != previous else last_change
        previous = e

    return max(longest, counter)


assert longest_of_two([1, 2, 3, 3, 1, 3, 5]) == 4
assert longest_of_two([2, 1, 2, 3, 3, 1, 3, 5]) == 4
assert longest_of_two([2, 1, 2, 3, 3, 2, 3, 5]) == 5
assert longest_of_two([2, 1, 2, 2, 3, 3, 2, 3, 5]) == 6
assert longest_of_two([2, 1, 2, 2, 2, 1, 2, 1]) == 8
assert longest_of_two([4, 3, 2, 1]) == 2
