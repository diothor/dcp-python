from graph_problems.problem_255.transitive_closure import transitive_closure


def test_matrix_size():
    dummy_list = [''] * 4
    closure = transitive_closure(dummy_list)
    assert len(closure) == 4
    assert len(closure[0]) == 4

    dummy_list = [''] * 8
    closure = transitive_closure(dummy_list)
    assert len(closure) == 8
    assert len(closure[0]) == 8


def test_diagonal_is_filled():
    graph = [[0] * 12] * 12
    closure = transitive_closure(graph)
    for i in range(12):
        assert closure[i][i] == 1


def test_problem_255():
    graph = [
        [0, 1, 3],
        [1, 2],
        [2],
        [3]
    ]

    expected = [
        [1, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    actual = transitive_closure(graph)
    print('\n')
    assert actual == expected


def test_from_geeks_for_geeks():
    graph = [
        [0, 1, 2],
        [1, 2],
        [0, 2, 3],
        [3]
    ]

    expected = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]

    actual = transitive_closure(graph)
    assert actual == expected


def test_for_two_transitions():
    graph = [
        [0, 1, 2],
        [1, 2],
        [0, 2, 3],
        [3, 4],
        [4]
    ]

    expected = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1]
    ]

    actual = transitive_closure(graph)
    assert actual == expected
