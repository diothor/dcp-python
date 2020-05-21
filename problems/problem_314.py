def broadcast_range(listeners: list, towers: list) -> int:
    min_range = 0

    prev_tower = None
    next_tower = towers[0]
    tower_index = 0

    # O(n) where n is number of listeners equal to len(listeners)
    for listener in listeners:
        if listener > next_tower:
            prev_tower = next_tower
            tower_index += 1
            next_tower = towers[tower_index] if tower_index < len(towers) else None

        dist_to_prev = listener - prev_tower if prev_tower is not None else float('inf')
        dist_to_next = next_tower - listener if next_tower is not None else float('inf')
        range_to_listener = min(dist_to_prev, dist_to_next)
        min_range = max(min_range, range_to_listener)

    return min_range


assert broadcast_range([1, 5, 11, 20], [4, 8, 15]) == 5
