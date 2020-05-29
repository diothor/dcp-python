def distinct_char_window(string: str) -> int:
    letters = set()
    for letter in string:
        letters.add(letter)

    letter_count = {}
    window = len(string)
    start = 0
    end = 0
    for index, letter in enumerate(string):
        letter_count[letter] = letter_count.setdefault(letter, 0) + 1
        end = index

        if letter_count.keys() == letters:
            first_letter = string[start]
            while letter_count[first_letter] > 1:
                letter_count[first_letter] -= 1
                start += 1
                first_letter = string[start]
            else:
                window = min(window, end - start + 1)

    return window


assert distinct_char_window('jiujitsu') == 5
assert distinct_char_window('aabcbcdbca') == 4
assert distinct_char_window('aabcbcdb') == 6
