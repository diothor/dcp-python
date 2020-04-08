from problem_269 import push_dominoes_simple, push_dominoes_elegant, push_dominoes_force
import pytest


@pytest.fixture(params=[push_dominoes_simple, push_dominoes_elegant, push_dominoes_force])
def push_foo(request):
    return request.param


def test_both_right(push_foo):
    assert push_foo('R...R') == 'RRRRR'


def test_both_left(push_foo):
    assert push_foo('L..L') == 'LLLL'


def test_left_right(push_foo):
    assert push_foo('L..R') == 'L..R'


def test_right_left(push_foo):
    assert push_foo('R...L') == 'RR.LL'


def test_doubles(push_foo):
    assert push_foo('RL..RL') == 'RL..RL'


def test_two_sections(push_foo):
    assert push_foo('R..LR..L') == 'RRLLRRLL'


def test_empty_edges(push_foo):
    assert push_foo('.L.R...LR..L..') == 'LL.RR.LLRRLL..'


def test_right_in_middle(push_foo):
    assert push_foo('.L.R....L') == 'LL.RRRLLL'


def test_left_in_middle(push_foo):
    assert push_foo('..R...L.L') == '..RR.LLLL'
