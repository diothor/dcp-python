from typing import List


def ones_at_front(num: int, nbits) -> int:
    bit_mask = 2 ** (nbits - 1)
    nones = 0
    while num & bit_mask > 0:
        nones += 1
        bit_mask >>= 1
    else:
        return nones


assert ones_at_front(0b0, 1) == 0
assert ones_at_front(0b01, 2) == 0
assert ones_at_front(0b10, 2) == 1
assert ones_at_front(0b1110, 4) == 3
assert ones_at_front(0b1111, 4) == 4
assert ones_at_front(0b1110, 2) == 1


def bytes_in_word(_byte: int) -> int:
    ones = ones_at_front(_byte, 8)
    if ones == 1 or ones > 4:
        raise ValueError
    else:
        return max(ones, 1)


# O(n) where n is number of bytes to check
def valid_utf8_encoding(bytes_to_check: List[int], start: int = 0, size: int = -1) -> bool:
    if size < 0:
        size = len(bytes_to_check)

    if size <= start:
        return True
    try:
        count = bytes_in_word(bytes_to_check[start])
        for i in range(start + 1, start + count):
            if bytes_to_check[i] & 0b11000000 != 0b10000000:
                return False
        else:
            return valid_utf8_encoding(bytes_to_check, start + count, size)
    except (ValueError, IndexError):
        return False


# acceptance cases
assert valid_utf8_encoding([0b11100010, 0b10000010, 0b10101100]) is True
assert valid_utf8_encoding([]) is True
assert valid_utf8_encoding([197, 130, 1]) is True
assert valid_utf8_encoding([235, 140, 4]) is False

# 1 byte case
assert valid_utf8_encoding([0]) is True
assert valid_utf8_encoding([127]) is True
assert valid_utf8_encoding([128]) is False
assert valid_utf8_encoding([255]) is False

# 2 byte case
assert valid_utf8_encoding([0b11011111, 0b10111111]) is True
assert valid_utf8_encoding([0b11011111, 0b10111111, 0b10111111]) is False
assert valid_utf8_encoding([0b11011111]) is False

# 3 byte case
assert valid_utf8_encoding([0b11101111, 0b10100011, 0b10111111]) is True
assert valid_utf8_encoding([0b11101111, 0b10100011, 0b10111111, 0b10100011]) is False
assert valid_utf8_encoding([0b11101111, 0b10100011]) is False

# 4 byte case
assert valid_utf8_encoding([0b11110001, 0b10101010, 0b10111111, 0b10101010]) is True
assert valid_utf8_encoding([0b11110001, 0b10100011, 0b10111111, 0b10100011, 0b10101010]) is False
assert valid_utf8_encoding([0b11110001, 0b10100011, 0b10101010]) is False

# wrong first byte header
assert valid_utf8_encoding([0b10000001, 0b10000001]) is False
assert valid_utf8_encoding([0b11111111, 0b10000001, 0b10000001, 0b10000001]) is False

# wrong next bytes header
assert valid_utf8_encoding([0b11110111, 0b01000001, 0b10000001, 0b10000001]) is False
assert valid_utf8_encoding([0b11110111, 0b10000001, 0b00000001, 0b10000001]) is False
assert valid_utf8_encoding([0b11110111, 0b10000001, 0b10000001, 0b11000001]) is False
