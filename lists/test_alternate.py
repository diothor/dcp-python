from sort import alternate


def test_from_dcp():
    asc = [i for i in range(1, 6)]
    alternate(asc)
    assert asc == [1, 3, 2, 5, 4]


def test_from_techiedelight():
    asc = [i for i in range(1, 8)]
    alternate(asc)
    assert asc == [1, 3, 2, 5, 4, 7, 6]


def test_from_techiedelight_shuffled():
    asc = [9, 6, 8, 3, 7]
    alternate(asc)
    assert asc == [6, 9, 3, 8, 7]
