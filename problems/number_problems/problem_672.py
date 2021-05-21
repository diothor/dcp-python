# O(n)
def max_path_weight(arr: list) -> int:
    weights = [0]
    for row in arr:
        row_weights = []
        for inum, num in enumerate(row):
            num_weights = [num + weights[i] for i in [inum - 1, inum] if 0 <= i < len(weights)]
            row_weights.append(max(num_weights))
        else:
            weights = row_weights
    else:
        return max(weights)


assert max_path_weight([
    [1],
    [2, 3],
    [1, 5, 1]
]) == 9

assert max_path_weight([
    [1],
    [2, 1],
    [1, 1, 1],
    [1, 1, 1, 3],
]) == 6

assert max_path_weight([
    [1],
    [2, 1],
    [1, 1, 1],
    [1, 1, 3, 1],
]) == 7
