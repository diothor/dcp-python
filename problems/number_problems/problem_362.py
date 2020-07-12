from typing import Tuple


def is_strobogrammatic(n: int, add_lead_zeros: bool = False) -> Tuple[int, ...]:
    if n < 1:
        return ()
    elif n == 1:
        return 0, 1, 8
    elif n == 2:
        zeros = (0,) if add_lead_zeros else tuple()
        return zeros + (11, 69, 88, 96)

    edges = tuple(divmod(e, 10) for e in is_strobogrammatic(2, add_lead_zeros))
    cores = is_strobogrammatic(n - 2, True)
    return tuple(10**(n-1) * left + 10 * middle + right for left, right in edges for middle in cores)


assert is_strobogrammatic(-100) == ()
assert is_strobogrammatic(0) == ()
assert is_strobogrammatic(1) == (0, 1, 8)
assert is_strobogrammatic(2) == (11, 69, 88, 96)
assert is_strobogrammatic(3) == (101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986)
assert is_strobogrammatic(4) == (1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966)

assert is_strobogrammatic(6) == (100001, 101101, 106901, 108801, 109601, 110011, 111111, 116911, 118811, 119611, 160091, 161191, 166991, 168891, 169691, 180081, 181181, 186981, 188881, 189681, 190061, 191161, 196961, 198861, 199661, 600009,
                                 601109, 606909, 608809, 609609, 610019, 611119, 616919, 618819, 619619, 660099, 661199, 666999, 668899, 669699, 680089, 681189, 686989, 688889, 689689, 690069, 691169, 696969, 698869, 699669, 800008, 801108,
                                 806908, 808808, 809608, 810018, 811118, 816918, 818818, 819618, 860098, 861198, 866998, 868898, 869698, 880088, 881188, 886988, 888888, 889688, 890068, 891168, 896968, 898868, 899668, 900006, 901106, 906906,
                                 908806, 909606, 910016, 911116, 916916, 918816, 919616, 960096, 961196, 966996, 968896, 969696, 980086, 981186, 986986, 988886, 989686, 990066, 991166, 996966, 998866, 999666)
