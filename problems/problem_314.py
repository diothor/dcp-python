def broadcast_range(listeners: list, towers: list) -> int:
    min_range = 0

    prev_tower = -float('inf')
    next_tower = towers[0]
    tower_index = 0

    # n is number of listeners equal to len(listeners)
    # k is number of  towers equal to len(towers)
    # O(n+k)
    for listener in listeners:
        while listener > next_tower:
            prev_tower = next_tower
            tower_index += 1
            next_tower = towers[tower_index] if tower_index < len(towers) else float('inf')

        dist_to_list = min(listener - prev_tower,  next_tower - listener)
        min_range = max(min_range, dist_to_list)
    return min_range


assert broadcast_range([0], [2]) == 2
assert broadcast_range([2], [1, 2, 3]) == 0
assert broadcast_range([4], [1, 2, 3]) == 1
assert broadcast_range([1, 5, 11, 20], [4, 8, 15]) == 5
