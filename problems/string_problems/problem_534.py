from collections import Counter


# O(n) + O(k) + O(2) ~= O(n)
def possible_palindrome(string: str) -> bool:
    letter_frequencies = Counter(string)  # O(n) where n is lenght of the string
    if sum(letter_frequencies.values()) < 2:  # O(k) where k is number of unique letters in the string
        return False
    odd_letters = filter(lambda f: f % 2 == 1, letter_frequencies.values())  # even_letters is an iterator so no opaeration is performed here, just the iterator definition has been created
    return next(odd_letters, None) is None or next(odd_letters, None) is None  # O(2)


# test cases from the task
assert possible_palindrome('carrace') is True
assert possible_palindrome('daily') is False
# no even letter case
assert possible_palindrome('aabb') is True
# even letter more than twice
assert possible_palindrome('aaaabb') is True
assert possible_palindrome('aaaabbc') is True
assert possible_palindrome('aaaabbcd') is False
# odd letter more than once
assert possible_palindrome('aaaabbbc') is False
# empty string
assert possible_palindrome('') is False
# single letter
assert possible_palindrome('a') is False
# two letters
assert possible_palindrome('aa') is True
assert possible_palindrome('ab') is False
