# O(n)
def smallex(s: str, k: int) -> str:
    if len(s) < 2:
        return s
    elif k > 1:
        return ''.join(sorted(s))

    lowest = 0
    for i in range(1, len(s)):
        if s[i] < s[lowest]:
            lowest = i
        elif s[i] == s[lowest]:
            j = 1
            while s[i + j] == s[lowest + j]:
                j += 1
            else:
                lowest = i if s[i + j] < s[lowest + j] else lowest
    else:
        return s[lowest:] + s[:lowest]


assert smallex('bac', 2) == 'abc'
assert smallex('ggggaaaccbb', 2) == 'aaabbccgggg'
assert smallex('gaurang', 3) == 'aaggnru'
assert smallex('uagrang', 3) == 'aaggnru'

assert smallex('kuh', 1) == 'hku'
assert smallex('kuhyhx', 1) == 'hxkuhy'
assert smallex('uagrang', 1) == 'agrangu'
assert smallex('daily', 1) == 'ailyd'

assert smallex('a', 7) == 'a'
