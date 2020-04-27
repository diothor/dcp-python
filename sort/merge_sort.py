def merge_sort(arr: list):
    if type(arr) != list:
        raise ValueError('Sorting takes only lists')
    elif len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    li, ri, ai = 0, 0, 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            arr[ai] = left[li]
            li += 1
        else:
            arr[ai] = right[ri]
            ri += 1
        ai += 1
    else:
        arr[ai:] = left[li:] if li < len(left) else right[ri:]
    return arr
