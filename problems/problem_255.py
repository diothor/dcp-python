class Person:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'v:{self.value}'

    def jump(self, steps):
        res = self.next
        for i in range(1, steps):
            res = res.next
            if res is None:
                return res
        else:
            return res


# O(2n) + O(n-1) ~= O(n)
def josephus(n: int, k: int) -> int:
    # O(2n)
    ppl = [Person(p) for p in range(1, n + 1)]  # O(n)
    for c, n in zip(ppl, ppl[1:]):  # O(n)
        c.next, n.prev = n, c
    ppl[0].prev, ppl[-1].next = ppl[-1], ppl[0]

    to_kill = ppl[k-1]
    # O(n-1)
    while to_kill != to_kill.next:  # O(n-1)
        to_kill.prev.next, to_kill.next.prev = to_kill.next, to_kill.prev  # O(1)
        to_kill = to_kill.jump(k)  # O(1)
    return to_kill.value


assert josephus(5, 2) == 3
assert josephus(7, 3) == 4
