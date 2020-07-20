# O(n)
def consecutive_seq_len(*args: int) -> int:
    seq_max_len = 0
    num_hashes = {num for num in args}  # O(n)
    for num in num_hashes:  # 2*O(n)
        if num - 1 not in num_hashes:  # O(1)
            new_seq = 1
            while num + new_seq in num_hashes:  # O(1)
                new_seq += 1
            seq_max_len = max(seq_max_len, new_seq)  # O(1)
    else:
        return seq_max_len


assert consecutive_seq_len() == 0
assert consecutive_seq_len(966) == 1
assert consecutive_seq_len(3, 5) == 1
assert consecutive_seq_len(3, 4) == 2
assert consecutive_seq_len(5, 18, 3, 8, 4, 9) == 3
assert consecutive_seq_len(5, 2, 99, 3, 4, 1, 100) == 5

assert consecutive_seq_len(21, 12, 13, 3, 23, 22, 89123, 1, 24, 321321, 11, 31231) == 4
