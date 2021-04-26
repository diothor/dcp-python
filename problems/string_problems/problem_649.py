from typing import Optional


# O(n) where n is number of letters in string `s`
def recurring_char(s: str) -> Optional[str]:
    chars = set()
    for char in s:
        if char in chars:
            return char
        else:
            chars.add(char)
    else:
        return None


# Basic cases
assert recurring_char('a') is None
assert recurring_char('ab') is None
assert recurring_char('aba') == 'a'
assert recurring_char('abab') == 'a'
assert recurring_char('abba') == 'b'

# Acceptance cases
assert recurring_char('acbbac') == 'b'
assert recurring_char('abcdef') is None
