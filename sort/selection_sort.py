def selection_sort(arr):
    if type(arr) != list:
        raise ValueError('Sorting takes only lists')

    for outer in range(len(arr)):
        min_index = outer
        for inner in range(outer + 1, len(arr)):
            if arr[inner] < arr[min_index]:
                min_index = inner
        arr[outer], arr[min_index] = arr[min_index], arr[outer]
    return arr
