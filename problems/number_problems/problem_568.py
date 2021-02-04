# O(n)
def sort_squars(arr: list) -> list:
    size = len(arr)
    squars = [None] * size
    i_res = size - 1
    i_left = 0
    i_right = size - 1
    while i_left <= i_right:
        if abs(arr[i_left]) < abs(arr[i_right]):
            squars[i_res] = arr[i_right] ** 2
            i_right -= 1
        else:
            squars[i_res] = arr[i_left] ** 2
            i_left += 1
        i_res -= 1
    else:
        return squars


assert sort_squars([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
assert sort_squars([-6, -3, -1, 2, 4, 5]) == [1, 4, 9, 16, 25, 36]
assert sort_squars([-5, -4, -2, 0, 1]) == [0, 1, 4, 16, 25]
