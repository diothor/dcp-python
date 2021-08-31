# O(n) where n is len of the `s` string
def xs_before_ys_flips(s: str) -> int:
    flip_count = 0
    x_count = 0
    y_count = 0
    for index, letter in enumerate(s):
        if letter == 'x' and y_count > 0:
            x_count += 1
        elif letter == 'y' and x_count == 0:
            y_count += 1
        elif letter == 'y' and x_count > 0:
            flip_count += min(x_count, y_count)
            x_count, y_count = 0, 1
    else:
        if x_count > 0 and y_count > 0:
            flip_count += min(x_count, y_count)
        return flip_count


# basic tests
assert xs_before_ys_flips('x') == 0
assert xs_before_ys_flips('xx') == 0
assert xs_before_ys_flips('xy') == 0
assert xs_before_ys_flips('y') == 0
assert xs_before_ys_flips('yy') == 0
assert xs_before_ys_flips('yx') == 1

# border cases
assert xs_before_ys_flips('xxyxxy') == 1
assert xs_before_ys_flips('xxyyyxy') == 1
assert xs_before_ys_flips('xxyyyxxy') == 2
assert xs_before_ys_flips('xyssyxxyyxy') == 3

# acceptance tests
assert xs_before_ys_flips('xyxxxyxyy') == 2
assert xs_before_ys_flips('yxxyxy') == 2
assert xs_before_ys_flips('xxyxyxxy') == 2
