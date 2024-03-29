# O(n)
def is_palindrome(num: int) -> bool:
    org_num, reversed_num = num, 0
    while num > 0:
        num, digit = divmod(num, 10)
        reversed_num = reversed_num*10 + digit
    else:
        return org_num == reversed_num


assert is_palindrome(121) is True
assert is_palindrome(888) is True
assert is_palindrome(678) is False
assert is_palindrome(66) is True
assert is_palindrome(696) is True
assert is_palindrome(123321) is True
