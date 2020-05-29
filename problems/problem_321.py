from math import sqrt


def steps_to_one(num: int) -> int:
    steps = 0
    while num > 1:
        div = int(sqrt(num))
        while div > 1:
            if num % div == 0:
                break
            else:
                div -= 1
        num = num // div if div > 1 else num - 1
        steps += 1
    else:
        return steps


assert steps_to_one(7) == 4
assert steps_to_one(15) == 4
assert steps_to_one(17) == 4
assert steps_to_one(24) == 4
assert steps_to_one(50) == 5
assert steps_to_one(250) == 5
