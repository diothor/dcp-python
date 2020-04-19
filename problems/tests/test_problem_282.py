from problem_282 import has_pythagorean_triplet_hash, has_pythagorean_triplet_naive, has_pythagorean_triplet_sort
import pytest
import random


@pytest.fixture(params=[has_pythagorean_triplet_hash, has_pythagorean_triplet_sort, has_pythagorean_triplet_naive])
def has_pythagorean_triplet(request):
    return request.param


@pytest.fixture(scope='module')
def random_data():
    return random.sample(range(1, 1_000_000), 6_000)


def test_positive(has_pythagorean_triplet):
    assert has_pythagorean_triplet([3, 1, 4, 6, 5]) is True


def test_negative(has_pythagorean_triplet):
    assert has_pythagorean_triplet([10, 4, 6, 12, 5]) is False


def test_big_data(has_pythagorean_triplet, random_data):
    has_pythagorean_triplet(random_data)
