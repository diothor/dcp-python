# O(n) where n is length of the input string
def to_valid(parentheses: str) -> int:
    unclosed, unnecessary = 0, 0
    for p in parentheses:
        if p == '(':
            unclosed += 1
        elif p == ')' and unclosed > 0:
            unclosed -= 1
        elif p == ')':
            unnecessary += 1
    else:
        return unnecessary + unclosed


assert to_valid('') == 0
assert to_valid('(') == 1
assert to_valid(')') == 1
assert to_valid('()') == 0
assert to_valid('(()') == 1
assert to_valid('())') == 1
assert to_valid(')(') == 2
assert to_valid('()())()') == 1
