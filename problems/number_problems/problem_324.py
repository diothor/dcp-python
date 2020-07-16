# O(nlogn)
def mouse_to_hole(mice: list, holes: list) -> int:
    holes.sort()  # O(nlogn)
    mice.sort()  # O(nlogn)

    max_steps = 0
    for mouse, hole in zip(mice, holes):  # O(n)
        max_steps = max(max_steps, abs(mouse - hole))
    return max_steps


assert mouse_to_hole([4, -4, 2], [4, 0, 5]) == 4
assert mouse_to_hole([-10, -79, -79, 67, 93, -85, -28, -94], [-2, 9, 69, 25, -31, 23, 50, 78]) == 102
assert mouse_to_hole([1, 4, 9, 15], [10, -5, 0, 16]) == 6
