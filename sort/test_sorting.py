import pytest
from random import shuffle
from heap_sort import heap_sort
from selection_sort import selection_sort
from merge_sort import merge_sort


@pytest.fixture(params=[merge_sort, heap_sort, selection_sort])
def sort_alg(request):
    return request.param


@pytest.fixture(scope='module', params=[100, 1000, 10_000])
def random_data(request):
    size = request.param
    expected = list(range(size))
    to_test = expected.copy()
    shuffle(to_test)
    return {'to_test': to_test, 'expected': expected}


def test_empty_array(sort_alg):
    assert sort_alg([]) == []


def test_wrong_argument(sort_alg):
    with pytest.raises(ValueError):
        sort_alg(None)
    with pytest.raises(ValueError):
        sort_alg(1)


def test_sort_123(sort_alg):
    assert sort_alg([2, 3, 1]) == [1, 2, 3]


def test_sort_with_duplicates(sort_alg):
    assert sort_alg([10, 3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 10]


def test_from_programiz(sort_alg):
    assert sort_alg([10, 3, 76, 34, 23, 32]) == [3, 10, 23, 32, 34, 76]


def test_random(sort_alg, random_data):
    assert sort_alg(random_data['to_test']) == random_data['expected']
