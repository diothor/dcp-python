from problem_278 import trees, preorder
from operator import itemgetter


def test_empty():
    assert trees(0) == [None]


def test_for_2():
    result = trees(2)
    assert len(result) == 2
    print_result(result)


def test_for_3():
    result = trees(4, 1)
    assert len(result) == 5
    print_result(result)


def print_result(result):
    graphs = sorted(map(preorder, result), key=itemgetter(0, 1))
    print('\n')
    [print(g) for g in graphs]