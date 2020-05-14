import heapq


def sort_almost_sorted(arr: list, k: int) -> list:
    # O(k+1) + O(k) ~= O(k)
    heap = arr[:k + 1]  # O(k + 1)
    heapq.heapify(heap)  # O(k)

    # O(n) + O(n-k-1) * O(logk) ~= O(nlogk)
    index_to_sort = 0
    while heap:  # O(n)
        arr[index_to_sort] = heapq.heappop(heap)  # O(1)
        index_to_heap = index_to_sort + k + 1
        if index_to_heap < len(arr):
            # O(n-k-1)
            heapq.heappush(heap, arr[index_to_heap])  # O(logk)
        index_to_sort += 1
    return arr


assert sort_almost_sorted([6, 5, 3, 2, 8, 10, 9], 3) == [2, 3, 5, 6, 8, 9, 10]
assert sort_almost_sorted([10, 9, 8, 7, 4, 70, 60, 50], 4) == [4, 7, 8, 9, 10, 50, 60, 70]
