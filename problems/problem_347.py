# O(n)
def smallex(s: str, k: int) -> str:
    if k > 1:
        return ''.join(sorted(s))
    elif s[0] > s[1]:
        return smallex(s[1:] + s[0], 1)
    else:
        return s


assert smallex('bac', 2) == 'abc'
assert smallex('ggggaaaccbb', 2) == 'aaabbccgggg'
assert smallex('gaurang', 3) == 'aaggnru'
assert smallex('uagrang', 3) == 'aaggnru'

assert smallex('uagrang', 1) == 'agrangu'
assert smallex('daily', 1) == 'ailyd'
