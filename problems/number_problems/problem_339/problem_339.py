def three_to_sum(arr: list, k: int, size: int = 0) -> bool:
    if k == 0 and size == 3:
        return True
    elif k < 0 or size > 3:
        return False

    for i in range(len(arr)):
        arr_copy = arr.copy()
        num = arr_copy.pop(i)
        if three_to_sum(arr_copy, k - num, size + 1):
            return True
    else:
        return False
