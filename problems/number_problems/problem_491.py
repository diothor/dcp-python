# O(n)
def is_palindrome(num: int) -> bool:
    digits = []
    while num > 0:
        num, digit = divmod(num, 10)
        digits.append(digit)
    else:
        return digits == digits[::-1]


assert is_palindrome(121) is True
assert is_palindrome(888) is True
assert is_palindrome(678) is False
assert is_palindrome(66) is True
assert is_palindrome(696) is True
assert is_palindrome(123321) is True
