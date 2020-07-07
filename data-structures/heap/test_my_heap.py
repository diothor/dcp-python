from heap.my_heap import Heap


def test_building_heap():
    heap = Heap(2, 10, 4, 5).storage
    assert_heap(heap)
    assert heap == [2, 5, 4, 10]

    heap = Heap(3, 1, 6, 0).storage
    assert_heap(heap)
    assert heap == [0, 1, 6, 3]


def test_pop():
    heap = Heap(2, 3, 4, 5, 10)
    assert heap.pop() == 2
    assert_heap(heap.storage)
    assert heap.storage == [3, 5, 4, 10]


def test_push():
    heap = Heap()
    assert heap.push(3).storage == [3]
    assert heap.push(1).storage == [1, 3]
    assert heap.push(6).storage == [1, 3, 6]
    assert heap.push(0).storage == [0, 1, 6, 3]
    assert_heap(heap.storage)


def test_push_contained_value():
    heap = Heap(0, 1, 6, 3)
    assert heap.push(0).storage == [0, 0, 6, 3, 1]
    assert_heap(heap.storage)


def assert_heap(heap: list):
    size = len(heap)
    for i in range(size):
        nodes = [heap[i]]
        left_index = 2 * i + 1
        if left_index < size:
            nodes.append(heap[left_index])
        right_index = left_index + 1
        if right_index < size:
            nodes.append(heap[right_index])
        assert heap[i] == min(nodes), 'Parent is greater than children. [P, *L, *R] is {}'.format(nodes)
