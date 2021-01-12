# O(1)
def clock_hands_angle(hh_mm: str) -> int:
    hh, mm = map(int, hh_mm.split(':'))
    minute_hand = 360 / 60 * mm
    hour_hand = 360 / 12 * (hh % 12) + 360 / 12 * (mm / 60)
    angle = int(abs(minute_hand - hour_hand))
    return angle


assert clock_hands_angle('00:00') == 0
assert clock_hands_angle('03:00') == 90
assert clock_hands_angle('06:00') == 180
assert clock_hands_angle('09:00') == 270
assert clock_hands_angle('12:00') == 0
assert clock_hands_angle('12:30') == 165
assert clock_hands_angle('3:30') == 75

# 0 angle between the hands is when mm = 5.45*(hh%12)
assert clock_hands_angle('1:05') < 6
assert clock_hands_angle('2:11') < 6
assert clock_hands_angle('3:16') < 6
assert clock_hands_angle('4:21') < 6
assert clock_hands_angle('06:33') < 6
assert clock_hands_angle('11:59') < 6
