def flip_count(string: str) -> int:
    last_x = string.rfind('x')
    return 0 if last_x < 0 else string.count('y', 0, last_x)


assert flip_count('xyxxxyxyy') == 2
assert flip_count('yyx') == 2
assert flip_count('xyxxxyxyyx') == 4
assert flip_count('xyxxxyxyyxxx') == 4
assert flip_count('yyxxx') == 2
assert flip_count('yyy') == 0
assert flip_count('xyy') == 0
assert flip_count('xxx') == 0
