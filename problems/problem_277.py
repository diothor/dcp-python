def is_utf8(byte_arr: list) -> bool:
    byte_index = 0
    while byte_index < len(byte_arr):
        leading_ones = 0
        while byte_arr[byte_index] << leading_ones & 128 == 128:
            leading_ones += 1

        if leading_ones > 4:
            return False
        elif byte_index + leading_ones > len(byte_arr):
            return False
        elif any(byte & 192 != 128 for byte in byte_arr[byte_index + 1:byte_index + leading_ones]):
            return False

        byte_index += leading_ones if leading_ones > 0 else 1
    else:
        return True if byte_arr else False


assert is_utf8([]) is False
assert is_utf8([0b11111111]) is False
assert is_utf8([0b01111111]) is True
assert is_utf8([0b11011111, 0b10111111]) is True
assert is_utf8([0b11111111, 0b11111111]) is False
assert is_utf8([0b11111111, 0b01111111]) is False
assert is_utf8([0b11111111, 0b00111111]) is False

assert is_utf8([197, 130, 1]) is True
assert is_utf8([235, 140, 4]) is False
