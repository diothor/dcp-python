from collections import deque


def alphabetical_id(col: int) -> str:
    char_offset = 64
    char_count = 26
    letters = deque()

    while col > 0:
        multiple, rest = divmod(col, char_count)
        if rest == 0:
            letters.appendleft('Z')
            multiple -= 1
        else:
            letters.appendleft(chr(char_offset + rest))
        col = multiple
    else:
        return ''.join(letters)


assert alphabetical_id(1) == 'A'
assert alphabetical_id(27) == 'AA'

assert alphabetical_id(2) == 'B'
assert alphabetical_id(25) == 'Y'
assert alphabetical_id(26) == 'Z'

assert alphabetical_id(28) == 'AB'
assert alphabetical_id(2*26) == 'AZ'
assert alphabetical_id(2*26+1) == 'BA'

assert alphabetical_id(26 * 26 * 2 + 26 * 4 + 3) == 'BDC'

# from geeksforgeeks
assert alphabetical_id(26) == 'Z'
assert alphabetical_id(51) == 'AY'
assert alphabetical_id(52) == 'AZ'
assert alphabetical_id(80) == 'CB'
assert alphabetical_id(676) == 'YZ'
assert alphabetical_id(702) == 'ZZ'
assert alphabetical_id(705) == 'AAC'
