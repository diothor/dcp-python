def flip_count(string: str) -> int:
    flips = 0
    y_count = 0
    for letter in string:
        if letter == 'y':
            y_count += 1
        elif letter == 'x' and y_count > 0:
            flips += y_count
            y_count = 0
    else:
        return flips


assert flip_count('xyxxxyxyy') == 2
assert flip_count('yyx') == 2
assert flip_count('xyxxxyxyyx') == 4
assert flip_count('xyxxxyxyyxxx') == 4
assert flip_count('yyxxx') == 2
