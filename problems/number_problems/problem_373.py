# O(nlogn)
def consecutive_seq_len(*args: int) -> int:
    nums_sorted = sorted(args)  # O(nlogn)
    seq_start = 0
    seq_max_len = 0
    for num_index in range(1, len(nums_sorted) + 1):  # O(n)
        prev = nums_sorted[num_index - 1]
        current = nums_sorted[num_index] if num_index < len(nums_sorted) else float('inf')
        if prev + 1 != current:
            seq_max_len = max(seq_max_len, num_index - seq_start)
            seq_start = num_index
    else:
        return seq_max_len


assert consecutive_seq_len() == 0
assert consecutive_seq_len(966) == 1
assert consecutive_seq_len(3, 5) == 1
assert consecutive_seq_len(3, 4) == 2
assert consecutive_seq_len(5, 18, 3, 8, 4, 9) == 3
assert consecutive_seq_len(5, 2, 99, 3, 4, 1, 100) == 5

assert consecutive_seq_len(21, 12, 13, 3, 23, 22, 89123, 1, 24, 321321, 11, 31231) == 4
