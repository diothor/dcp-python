from problem_257 import find_unsorted_part


def test_from_dcp():
    assert find_unsorted_part([3, 7, 5, 6, 9]) == (1, 3)


def test_from_geek_for_geeks():
    assert find_unsorted_part([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]) == (3, 8)
    assert find_unsorted_part([0, 1, 15, 25, 6, 7, 30, 40, 50]) == (2, 5)


def test_tricky():
    assert find_unsorted_part([3, 7, 5, 6, 7, 1, 9]) == (0, 5)
