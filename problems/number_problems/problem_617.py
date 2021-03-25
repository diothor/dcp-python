roman_nums = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


# O(n) where n is number of letters in roman number
def roman_dec(roman: str) -> int:
    heighest = 0
    dec = 0
    for letter in reversed(roman):
        if letter not in roman_nums:
            raise ValueError(f'Inproper character `{letter}` in roman number `{roman}`')
        num = roman_nums[letter]
        if num < heighest:
            dec -= num
        else:
            dec += num
            heighest = num
    else:
        return dec


# single letter
assert roman_dec('I') == 1
assert roman_dec('C') == 100

# sum of all
assert roman_dec('II') == 2
assert roman_dec('VI') == 6
assert roman_dec('XIII') == 13
assert roman_dec('MDCLXVI') == 1666

# substract
assert roman_dec('IV') == 4
assert roman_dec('IIC') == 98
assert roman_dec('VX') == 5
assert roman_dec('IVX') == 4  # !!!! Online calcs give an error here. It looks strange, too.
assert roman_dec('VIX') == 4  # !!!! Online calcs give an error here. However, it looks ok.
assert roman_dec('XLV') == 45
assert roman_dec('XXIIX') == 28
assert roman_dec('MMXLVIX') == 2044

# bad input
assert roman_dec('') == 0
try:
    assert roman_dec('H')
    assert False
except ValueError as e:
    pass

# from wiki
assert roman_dec('XXXIX') == 39
assert roman_dec('CCXLVI') == 246
assert roman_dec('DCCLXXXIX') == 789
assert roman_dec('MMCDXXI') == 2421

assert roman_dec('CLX') == 160
assert roman_dec('CCVII') == 207
assert roman_dec('MIX') == 1009
assert roman_dec('MLXVI') == 1066

assert roman_dec('MDCCLXXVI') == 1776
assert roman_dec('MCMXVIII') == 1918
assert roman_dec('MCMLIV') == 1954
assert roman_dec('MMXIV') == 2014
