from operator import itemgetter


def heap_sort(arr: list):
    if type(arr) != list:
        raise ValueError('Sorting takes only lists')

    __build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        __heapify_down(arr, i)
    return arr


def __heapify_down(heap: list, heap_size: int, index=0):
    family = [(i, heap[i]) for i in [index, 2 * index + 1, 2 * index + 2] if i < heap_size]
    biggest = max(family, key=itemgetter(1, 0), default=None)
    if biggest and biggest[0] is not index:
        heap[index], heap[biggest[0]] = heap[biggest[0]], heap[index]
        __heapify_down(heap, heap_size, biggest[0])


def __build_heap(arr: list):
    size = len(arr)
    for i in range(size // 2 - 1, -1, -1):
        __heapify_down(arr, size, i)
