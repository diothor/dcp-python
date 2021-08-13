# O(n+m) where n is length of shift_from and m is length is length of shift_to
def can_be_shifted(shift_from: str, shift_to: str) -> bool:
    return shift_from in (shift_to + shift_to)


assert can_be_shifted('abcde', 'cdeab') is True
assert can_be_shifted('abc', 'acb') is False
