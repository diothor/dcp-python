def josephus(n: int, k: int) -> int:
    ppl = [p for p in range(1, n + 1)]
    kill_place = k - 1

    # O(n-1)*O(n) ~= O(n^2)
    while len(ppl) > 1:  # O(n-1)
        del(ppl[kill_place])  # O(n)
        kill_place = (kill_place + k - 1) % len(ppl)  # O(1)
    return ppl.pop()


assert josephus(5, 2) == 3
assert josephus(7, 3) == 4
