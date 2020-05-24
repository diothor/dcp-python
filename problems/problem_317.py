def msb_index(num: int) -> int:
    msb = -1
    while num > 0:
        msb += 1
        num = num >> 1
    return msb


def bitwise_and(from_num: int, to_num: int) -> int:
    msb_from = msb_index(from_num)
    msb_to = msb_index(to_num)

    if msb_to != msb_from:
        return 0

    shift = 1 << msb_from
    return shift + bitwise_and(from_num - shift, to_num - shift)


assert bitwise_and(17, 19) == 16
assert bitwise_and(4, 7) == 4
assert bitwise_and(12, 15) == 12
assert bitwise_and(10, 20) == 0
assert bitwise_and(11, 21) == 0
