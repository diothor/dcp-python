def jumps_to(n: int) -> int:
    jump, value = 0, 0
    while value < n or (value - n) & 1:
        jump += 1
        value += jump
    return jump


assert jumps_to(1) == 1
assert jumps_to(2) == 3
assert jumps_to(3) == 2
assert jumps_to(8) == 4
assert jumps_to(9) == 5
