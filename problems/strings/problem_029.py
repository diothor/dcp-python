def run_length_encode(s: str) -> str:
    if s == '':
        return s

    encoded = ''
    current = s[0]
    counter = 0

    def encode_current():
        return str(counter) + current

    for letter in s:
        if letter != current:
            encoded += encode_current()
            current = letter
            counter = 0
        counter += 1

    return encoded + encode_current()


def run_length_decode(s: str) -> str:
    if s == '':
        return s

    decoded = ''
    counter = ''
    for letter in s:
        if letter.isdigit():
            counter += letter
        else:
            decoded += letter * int(counter)
            counter = ''
    return decoded


actual = run_length_encode('AAAABBBCCDAA')
assert actual == '4A3B2C1D2A', actual

actual = run_length_decode('4A3B2C1D2A')
assert actual == 'AAAABBBCCDAA', actual
