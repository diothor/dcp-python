def has_pythagorean_triplet_naive(nums: list) -> bool:
    for a in nums:
        a = a ** 2
        for b in nums:
            b = b ** 2
            for c in nums:
                if a + b == c ** 2:
                    return True
    else:
        return False


def has_pythagorean_triplet_hash(nums: list) -> bool:
    squares_set = {n ** 2: n for n in nums}
    squares_list = list(squares_set.keys())
    for ia, a in enumerate(squares_list):
        del(squares_list[ia])
        for b in squares_list:
            if a + b in squares_set:
                return True
    else:
        return False


def has_pythagorean_triplet_sort(nums: list) -> bool:
    squares = [n ** 2 for n in nums]
    squares.sort()

    for ic in range(len(nums) - 1, -1, -1):
        ia = 0
        ib = ic - 1 if ic > 0 else 0
        while ia <= ib:
            if squares[ia] + squares[ib] == squares[ic]:
                return True
            elif squares[ia] + squares[ib] < squares[ic]:
                ia += 1
            elif squares[ia] + squares[ib] > squares[ic]:
                ib -= 1
    else:
        return False
