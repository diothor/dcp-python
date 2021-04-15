# O(n) where n = last - first
def _reverse_arr(arr: list, first: int, last: int, skip: set = None) -> None:
    if skip is None:
        skip = set()
    while first < last:
        if arr[first] in skip:
            first += 1
        elif arr[last] in skip:
            last -= 1
        else:
            arr[first], arr[last] = arr[last], arr[first]
            first += 1
            last -= 1


# O(n) where n is number of letters in s
def reverse_words(s: str) -> str:
    letters = [let for let in s]
    size = len(letters)

    w_start, w_end = 0, letters.index(' ')
    while w_start < size - 1:
        _reverse_arr(letters, w_start, w_end, skip={' '})
        w_start = w_end
        try:
            w_end = letters.index(' ', w_start + 1)
        except ValueError:
            w_end = size - 1
    else:
        _reverse_arr(letters, 0, size - 1)
        return ''.join(letters)


assert reverse_words(' hello world here') == 'here world hello '

assert reverse_words('geeks quiz practice code') == 'code practice quiz geeks'
assert reverse_words('getting good at coding needs a lot of practice') == 'practice of lot a needs coding at good getting'

assert reverse_words('   ') == '   '
assert reverse_words('  space before') == 'before space  '
assert reverse_words('space after ') == ' after space'
