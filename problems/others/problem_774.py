from io import TextIOBase, StringIO


def read7(src: TextIOBase, dst: StringIO = None) -> int:
    if dst is None:
        dst = StringIO()
    content = src.read(7)
    dst.write(content)
    return len(content)


# O(n)
def read_n(n: int, src: TextIOBase, dst: StringIO = None) -> int:
    if dst is None:
        dst = StringIO()
    eof = False
    all_chars = 0
    while not eof and all_chars < n:
        current_chars = read7(src, dst)
        if current_chars < 7:
            eof = True
        all_chars += current_chars
        if all_chars > n:
            dst.truncate(n)
            all_chars = n
    else:
        return all_chars


assert read_n(6, StringIO('1234567')) == 6
assert read_n(7, StringIO('1234567')) == 7
assert read_n(8, StringIO('1234567')) == 7

assert read_n(7, StringIO('12345678')) == 7
assert read_n(1, StringIO('')) == 0
assert read_n(5, StringIO('123')) == 3
