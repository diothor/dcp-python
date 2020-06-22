def common_fraction(n: str) -> tuple:
    if '/' in n:
        a, b = map(int, n.split('/'))
        return a, b
    elif '.' in n:
        whole, fraction = n.split('.')
        a, b = int(fraction), 10**len(fraction)
        a += int(whole) * b
        return a, b
    else:
        return int(n), 1


def egyptian_fractions(num: int, den: int, res: list = None) -> list:
    if res is None:
        res = []
    if num < 1:
        return res

    fraction = den // num if den % num == 0 else den // num + 1
    res.append(f'1/{fraction}')
    num = fraction * num - den
    den = fraction * den
    return egyptian_fractions(num, den, res)


def decompose(n):
    num, den = common_fraction(n)
    res = []
    if num > den:
        fraction, num = divmod(num, den)
        res.append(f'{fraction}')
    return egyptian_fractions(num, den, res)


assert egyptian_fractions(16, 17) == ['1/2', '1/3', '1/10', '1/128', '1/32640']
assert egyptian_fractions(3, 4) == ['1/2', '1/4']
assert decompose('0.66') == ["1/2", "1/7", "1/59", "1/5163", "1/53307975"]
assert decompose('75/3') == ['25']
assert decompose('7.989') == ['7', '1/2', '1/3', '1/7', '1/79', '1/6610', '1/99690819', '1/12146761380509000']
assert egyptian_fractions(100, 4187) == ['1/42', '1/13528', '1/237895292', '1/70742712206811288']
assert decompose('0') == []
assert decompose('3/4') == ["1/2", "1/4"]
assert decompose('10') == ['10']

