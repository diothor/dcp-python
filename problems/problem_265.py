def bonuses(coders: list) -> list:
    size = len(coders)
    rewards = [1] * size

    for index in range(1, size):
        if coders[index] > coders[index - 1]:
            rewards[index] = rewards[index - 1] + 1

    for index in range(size - 2, -1, -1):
        if coders[index] > coders[index + 1]:
            rewards[index] = max(rewards[index], rewards[index + 1] + 1)

    return rewards


a = bonuses([10, 40, 200, 1000, 60, 30])
assert a == [1, 2, 3, 4, 2, 1], a

b = bonuses([10, 40, 10, 200, 1000, 60, 30])
assert b == [1, 2, 1, 2, 3, 2, 1], b

c = bonuses([40, 10, 200, 1000, 60, 30])
assert c == [2, 1, 2, 3, 2, 1], c

d = bonuses([4, 6, 4, 5, 6, 2])
assert d == [1, 2, 1, 2, 3, 1], d

e = bonuses([10, 10, 200, 1000, 60, 30])
assert e == [1, 1, 2, 3, 2, 1], e
