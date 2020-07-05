# O = C(n, 3)
def three_to_sum(arr: list, k: int) -> bool:
    size = len(arr)
    for x in range(size):
        for y in range(x + 1, size):
            for z in range(y + 1, size):
                if arr[x] + arr[y] + arr[z] == k:
                    return True
    else:
        return False
