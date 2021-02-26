import pytest
from stack_queue.max_in_stack import StackWithMax


@pytest.fixture
def max_stack():
    return StackWithMax()


def test_empty_stack(max_stack):
    assert max_stack.pop() is None
    assert max_stack.peek() is None
    assert max_stack.max() is None


def test_push(max_stack):
    assert max_stack.peek() is None

    max_stack.push(1)
    assert max_stack.peek() == 1
    assert max_stack.stack == [1]

    max_stack.push(3)
    assert max_stack.peek() == 3
    assert max_stack.stack == [1, 3]


def test_max(max_stack):
    assert max_stack.max() is None

    max_stack.push(3)
    assert max_stack.max() == 3

    max_stack.push(2)
    assert max_stack.max() == 3
    assert max_stack.max_value == [3, 3]

    max_stack.push(4)
    assert max_stack.max() == 4
    assert max_stack.max_value == [3, 3, 4]

    max_stack.pop()
    assert max_stack.max() == 3
    assert max_stack.max_value == [3, 3]

    max_stack.pop()
    assert max_stack.max() == 3

    max_stack.pop()
    assert max_stack.max() is None


def test_pop(max_stack):
    assert max_stack.pop() is None
    max_stack.push(2)
    max_stack.push(1)
    max_stack.push(3)

    assert max_stack.pop() == 3
    assert max_stack.pop() == 1
    assert max_stack.pop() == 2
    assert max_stack.pop() is None


def test_peek(max_stack):
    assert max_stack.peek() is None

    max_stack.push(3)
    assert max_stack.peek() == 3
    assert max_stack.peek() == 3

    max_stack.push(4)
    assert max_stack.peek() == 4
    assert max_stack.peek() == 4

    max_stack.push(2)
    assert max_stack.peek() == 2
    assert max_stack.peek() == 2

    max_stack.pop()
    assert max_stack.peek() == 4
