def throw_dice(throws: int, face_num: int, total: int) -> int:
    results = _throw(throws, face_num, total)
    return len(results)


def _throw(throws_left, face_num, to_total) -> list:
    results = []

    if throws_left == 1:
        for f in range(1, face_num + 1):
            if to_total - f == 0:
                results.append([f])
        return results

    for f in range(1, face_num + 1):
        sub_results = _throw(throws_left - 1, face_num, to_total - f)
        results += map(lambda l: [f] + l, sub_results)
    return results
