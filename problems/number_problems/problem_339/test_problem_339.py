from number_problems.problem_339.problem_339 import three_to_sum


def test_given_example():
    assert three_to_sum([20, 303, 3, 4, 25], 49) is True


def test_when_false():
    assert three_to_sum([20, 303, 3, 4, 25], 100) is False


def test_when_zero():
    assert three_to_sum([], 0) is False
    assert three_to_sum([20, 303, 3, 4, 25], 0) is False


def test_when_too_many_to_sum():
    assert three_to_sum([20, 303, 3, 2, 2, 25], 49) is False


def test_when_too_few_to_sum():
    assert three_to_sum([24, 303, 3, 25], 49) is False


def test_discontinuous_nums_when_sorted():
    assert three_to_sum([20, 303, 3, 4, 25, 7, 21], 49) is True


def test_if_one_number_is_used_once():
    assert three_to_sum([2, 4, 5], 6) is False
