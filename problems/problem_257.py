def find_unsorted_part(unsorted_list: list) -> tuple:
    size = len(unsorted_list)

    vmax = float('-inf')
    vmin = float('inf')

    istart = None
    iend = None
    for i in range(size):
        if unsorted_list[i] > vmax:
            vmax = unsorted_list[i]
        if unsorted_list[i] < vmax:
            iend = i

        if unsorted_list[size - 1 - i] < vmin:
            vmin = unsorted_list[size - 1 - i]
        if unsorted_list[size - 1 - i] > vmin:
            istart = size - 1 - i

    return istart, iend
