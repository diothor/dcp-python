from problem_279 import count_groups


def test_when_no_people():
    assert count_groups([]) == 0


def test_all_people_in_single_group():
    people = [
        [1, 2],
        [3, 4],
        [3],
        [4],
        [1],
    ]
    assert count_groups(people) == 1


def test_from_dcp():
    people = [
        [1, 2],
        [0, 5],
        [0],
        [6],
        [],
        [1],
        [3],
    ]
    assert count_groups(people) == 3
