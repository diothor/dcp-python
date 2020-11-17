import logging


# O(n)
def jumps(*steps: int) -> int:
    jumps_steps = [steps[0]]

    index = 1
    max_reach = steps[0]
    potential_reach = 0
    potential_step = None

    while max_reach < len(steps) - 1:
        reach = index + steps[index]
        if reach >= potential_reach:
            potential_reach = reach
            potential_step = steps[index]
        if index == max_reach:
            max_reach = potential_reach
            jumps_steps.append(potential_step)
            potential_reach, potential_step = 0, None
        index += 1
    else:
        logging.debug(f' --> steps: {jumps_steps}; looped {index}/{len(steps)} times')
        return len(jumps_steps)


logging.basicConfig(level=logging.DEBUG)
assert jumps(6, 2, 4, 0, 5, 1, 1, 4, 2, 9) == 2
assert jumps(1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9) == 3
assert jumps(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) == 10
