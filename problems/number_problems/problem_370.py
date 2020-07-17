# Not sure I understood the problem correclty. The given example should result in 1260 sec. Have no idea how they came with this number.


# O(n)
def active_time(*events) -> int:
    total_active_time = 0
    active_deliveries = {}
    for delivery, timestamp, action in events:
        if action == 'pickup':
            active_deliveries.setdefault(delivery, timestamp)
        elif action == 'dropoff':
            pickup_time = active_deliveries.pop(delivery)
            total_active_time += timestamp - pickup_time
    else:
        return total_active_time


assert active_time(
    (1, 1570320047, 'pickup'),
    (1, 1570320725, 'dropoff'),
    (2, 1570321092, 'pickup'),
    (3, 1570321212, 'pickup'),
    (3, 1570322352, 'dropoff'),
    (2, 1570323012, 'dropoff')
) == 3738
