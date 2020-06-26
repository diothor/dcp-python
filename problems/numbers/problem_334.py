def play24(*nums, start: int = 0, so_far: int = 0) -> bool:
    if start > len(nums) - 1:
        return 24 == so_far

    if start == 0:
        return play24(*nums, start=1, so_far=nums[0])

    this_round = [so_far + nums[start], so_far * nums[start], so_far - nums[start], so_far // nums[start]]
    for sub_res in this_round:
        if play24(*nums, start=start + 1, so_far=sub_res):
            return True
    else:
        return False


assert play24(1, 2, 3, 4) is True
assert play24(5, 2, 7, 8) is True
assert play24(4, 8, 3, 6) is True
assert play24(3, 9, 4, 10) is False
assert play24(1, 5, 5, 5) is False
