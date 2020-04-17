import pytest
from problem_276 import search_naive, search_kmp, longest_proper_prefixes


@pytest.fixture(params=[search_naive, search_kmp])
def search_engine(request):
    return request.param


def test_empty_string(search_engine):
    assert search_engine('', 'TEST') == []


def test_empty_pattern(search_engine):
    assert search_engine('string', '') == []


def test_no_match(search_engine):
    assert search_engine('THIS IS A TEST TEXT', 'NO MATCH') == []


def test_match_in_middle(search_engine):
    assert search_engine('THIS IS A TEST TEXT', 'TEST') == [10]


def test_multiple_matches(search_engine):
    assert search_engine('AABAACAADAABAABA', 'AABA') == [0, 9, 12]


def test_multiple_from_geek(search_engine):
    assert search_engine('AAAAABAAABA', 'AAAA') == [0, 1]


def test_pattern_distinct_letters_match(search_engine):
    pattern = 'ABCD'
    text = 'ABCD' * 500_000
    assert len(search_engine(text, pattern)) == 500_000


def test_pattern_distinct_letters_no_match(search_engine):
    text = 'ABCD' * 500_000
    assert search_engine(text, 'ABCDE') == []


def test_pattern_repeated_letters_full_match(search_engine):
    pattern = 'A' * 4
    text = 'A' * 500_000
    assert len(search_engine(text, pattern)) == len(text) - len(pattern) + 1


def test_very_long(search_engine):
    pattern = '1234567890'
    text = ('123456789' * 1000 + '0') * 10
    assert search_engine(text, pattern) == [8991, 17992, 26993, 35994, 44995, 53996, 62997, 71998, 80999, 90000]


def test_prefix_of_empty():
    assert longest_proper_prefixes('') == []


def test_prefix_of_single():
    assert longest_proper_prefixes('a') == [0]


def test_prefix_of_simple():
    assert longest_proper_prefixes('aba') == [0, 0, 1]
    assert longest_proper_prefixes('abab') == [0, 0, 1, 2]
    assert longest_proper_prefixes('abcab') == [0, 0, 0, 1, 2]
    assert longest_proper_prefixes('aaaa') == [0, 1, 2, 3]


def test_from_geeks():
    assert longest_proper_prefixes('AAACAAAA') == [0, 1, 2, 0, 1, 2, 3, 3]
