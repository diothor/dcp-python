from typing import List


# O(1)
def parse_octet(octet_str: str, octet_num: int = 0) -> List[str]:
    if not octet_str:
        return []
    if octet_str[0] == '0':
        return [] if octet_num == 0 else ['0']
    octet_values = []
    new_value = ''
    for digit in octet_str:  # O(3)
        new_value += digit
        if int(new_value) < 256:
            octet_values.append(new_value)
        else:
            break
    return octet_values


assert parse_octet('') == []
# single digit
assert parse_octet('1') == ['1']
assert parse_octet('9') == ['9']
assert parse_octet('0') == []
assert parse_octet('0', 1) == ['0']

# two digits
assert parse_octet('10') == ['1', '10']
assert parse_octet('99') == ['9', '99']
assert parse_octet('01') == []
assert parse_octet('01', 1) == ['0']

# three digits
assert parse_octet('100') == ['1', '10', '100']
assert parse_octet('255') == ['2', '25', '255']
assert parse_octet('256') == ['2', '25']
assert parse_octet('999') == ['9', '99']
assert parse_octet('011') == []
assert parse_octet('011', 1) == ['0']
assert parse_octet('001') == []
assert parse_octet('001', 1) == ['0']


# O(1)
def ips(digits: str, start: int = 0) -> List[str]:
    res = []
    frst_octet_values = parse_octet(digits[0:3], 0)
    # O(3)
    for v1 in frst_octet_values:
        snd_start = len(v1)
        snd_octet_values = parse_octet(digits[snd_start: snd_start + 3], 1)
        # O(3)
        for v2 in snd_octet_values:
            trd_start = snd_start + len(v2)
            trd_octet_values = parse_octet(digits[trd_start: trd_start + 3], 2)
            # O(3)
            for v3 in trd_octet_values:
                fth_start = trd_start + len(v3)
                fth_octet_values = parse_octet(digits[fth_start: fth_start + 3], 3)
                # O(3)
                for v4 in fth_octet_values:
                    fth_end = fth_start + len(v4)
                    if fth_end == len(digits):
                        res.append(f'{v1}.{v2}.{v3}.{v4}')
    else:
        return sorted(res)


# basic cases
assert ips('1234') == ['1.2.3.4']
assert ips('255255255255') == ['255.255.255.255']
assert ips('25525510255') == ['255.255.10.255', '255.255.102.55']
assert ips('2552550255') == ['255.25.50.255', '255.255.0.255']

# no-result cases
assert ips('123') == []
assert ips('02343') == []
assert ips('256255255255') == []
assert ips('255256255255') == []
assert ips('255255256255') == []
assert ips('255255255256') == []

# acceptance cases
assert ips('2542540123') == ['254.25.40.123', '254.254.0.123']
assert ips('25525511135') == ['255.255.11.135', '255.255.111.35']
assert ips('11111011111') == ['111.110.11.111', '111.110.111.11']
