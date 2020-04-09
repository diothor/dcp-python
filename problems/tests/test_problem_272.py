import my_decors
from problem_272 import throw_dice


def test_simple():
    assert throw_dice(3, 6, 7) == 15
    assert throw_dice(2, 4, 4) == 3
    assert throw_dice(3, 6, 12) == 25
    assert throw_dice(3, 8, 24) == 1


def test_when_imposible():
    assert throw_dice(4, 8, 2) == 0


@my_decors.timeit
def test_performance():
    assert throw_dice(8, 6, 48) == 1
