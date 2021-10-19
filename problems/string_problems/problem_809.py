# O(n) where n is lenght of input string
def balanced_brackets(string: str, brackets: dict = None) -> bool:
    if brackets is None:
        brackets = {'(': ')', '[': ']', '{': '}'}

    closings = {v for v in brackets.values()}
    stack = []

    for char in string:
        if char in brackets:
            stack.append(brackets[char])
        elif char in closings and (not stack or char != stack.pop()):
            return False
    else:
        return len(stack) < 1


# basic cases
assert balanced_brackets('()') is True
assert balanced_brackets('(') is False
assert balanced_brackets(')') is False
assert balanced_brackets('(())') is True
assert balanced_brackets('(()') is False
assert balanced_brackets('())') is False

# basic cases with chars between brackets
assert balanced_brackets('((a))') is True
assert balanced_brackets('(a())') is True
assert balanced_brackets('(())a') is True
assert balanced_brackets('a(a(a)a)a') is True

# acceptance cases
assert balanced_brackets('([])[]({})') is True
assert balanced_brackets('([)]') is False
assert balanced_brackets('((()') is False
