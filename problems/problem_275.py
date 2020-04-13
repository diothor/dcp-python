def look_and_say(term_num: int) -> str:
    term = '1'
    for i in range(1, term_num):
        next_term = ''
        count = 0
        current_letter = term[0]
        for letter in term:
            if letter == current_letter:
                count += 1
            else:
                next_term += str(count) + current_letter
                count = 1
                current_letter = letter
        term = next_term + str(count) + current_letter
    return term


assert look_and_say(1) == '1'
assert look_and_say(2) == '11'
assert look_and_say(3) == '21'
assert look_and_say(5) == '111221'
assert look_and_say(8) == '1113213211'
