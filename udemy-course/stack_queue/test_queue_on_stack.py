from stack_queue.queue_on_stack import QueueOnStack
import pytest


@pytest.fixture
def queue():
    return QueueOnStack()


def test_enqueue(queue):
    assert queue.front.is_empty() is True
    assert queue.rear.is_empty() is True

    queue.enqueue(0)
    assert queue.front.peek() == 0
    assert queue.front.is_empty() is False
    assert queue.rear.is_empty() is True

    queue.enqueue(1)
    assert queue.front.peek() == 1
    assert queue.front.stack == [0, 1]
    assert queue.rear.is_empty() is True

    queue.enqueue(0)
    assert queue.front.peek() == 0
    assert queue.front.stack == [0, 1, 0]
    assert queue.rear.is_empty() is True


def test_dequeue(queue):
    assert queue.dequeue() is None

    queue.enqueue(0).enqueue(1).enqueue(2)
    assert queue.front.stack == [0, 1, 2]
    assert queue.rear.is_empty() is True

    assert queue.dequeue() == 0
    assert queue.front.is_empty() is True
    assert queue.rear.stack == [2, 1]


def test_transfer_between_stacks(queue):
    queue.enqueue(100).enqueue(200)
    assert queue.dequeue() == 100
    assert queue.front.is_empty() is True
    assert queue.rear.stack == [200]

    queue.enqueue(300)
    assert queue.front.stack == [300]
    assert queue.rear.stack == [200]

    assert queue.dequeue() == 200
    assert queue.front.stack == [300]
    assert queue.rear.is_empty() is True

    assert queue.dequeue() == 300
    assert queue.front.is_empty() is True
    assert queue.rear.is_empty() is True

    assert queue.dequeue() is None
