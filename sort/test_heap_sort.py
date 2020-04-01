from heap_sort import heap_sort
from random import shuffle


def test_root():
    assert heap_sort([10, 3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 10]


def test_sort():
    assert heap_sort([2, 3, 1]) == [1, 2, 3]


def test_sort_programiz():
    assert heap_sort([10, 3, 76, 34, 23, 32]) == [3, 10, 23, 32, 34, 76]


def test_random():
    expected = list(range(100))
    under_test = expected.copy()
    shuffle(under_test)
    assert heap_sort(under_test) == expected
