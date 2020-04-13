from my_decors import timeit


@timeit
def fixed_point_linear(arr: list):
    fixed = [a for i, a in enumerate(arr) if i == a]
    return fixed[0] if fixed else False


@timeit
def fixed_point_binary(arr: list):
    first = 0
    last = len(arr) - 1
    while last != first:
        middle = (first + last) // 2
        if middle == arr[middle]:
            return middle
        if middle > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return False
