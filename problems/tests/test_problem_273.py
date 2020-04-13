import pytest
import random
import my_decors
from problem_273 import fixed_point_binary, fixed_point_linear


@pytest.fixture(scope='module')
@my_decors.timeit
def random_array():
    arr_size = 16_000_000 * 3
    return random.sample(range(-30_000_000, 30_000_000), arr_size)


@pytest.fixture(params=[fixed_point_linear, fixed_point_binary])
def fixed_point(request):
    return request.param


def test_simple(fixed_point):
    assert fixed_point([-6, 0, 2, 40]) == 2
    assert fixed_point([-10, -5, 0, 3, 7]) == 3
    assert fixed_point([1, 5, 7, 8]) is False


def test_performance(fixed_point, random_array):
    size = len(random_array)
    print(fixed_point(random_array[:size // 3]))
    print(fixed_point(random_array[:size // 2]))
    print(fixed_point(random_array))
