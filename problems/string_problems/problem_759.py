from typing import List, Tuple


# O(1)
def octet_permutations(octet_str: str, octet_num: int = 1) -> List[Tuple[str, int]]:
    if not octet_str:
        return []
    if octet_str[0] == '0':
        return [] if octet_num == 1 else [('0', 1)]
    permutations = []
    new_value = ''
    for index, digit in enumerate(octet_str):  # O(3)
        new_value += digit
        if int(new_value) < 256:
            permutations.append((new_value, index + 1))
        else:
            break
    return permutations


assert octet_permutations('') == []
# single digit
assert octet_permutations('1') == [('1', 1)]
assert octet_permutations('9') == [('9', 1)]
assert octet_permutations('0') == []
assert octet_permutations('0', 2) == [('0', 1)]

# two digits
assert octet_permutations('10') == [('1', 1), ('10', 2)]
assert octet_permutations('99') == [('9', 1), ('99', 2)]
assert octet_permutations('01') == []
assert octet_permutations('01', 2) == [('0', 1)]

# three digits
assert octet_permutations('100') == [('1', 1), ('10', 2), ('100', 3)]
assert octet_permutations('255') == [('2', 1), ('25', 2), ('255', 3)]
assert octet_permutations('256') == [('2', 1), ('25', 2)]
assert octet_permutations('999') == [('9', 1), ('99', 2)]
assert octet_permutations('011') == []
assert octet_permutations('011', 2) == [('0', 1)]
assert octet_permutations('001') == []
assert octet_permutations('001', 2) == [('0', 1)]


# O(1)
def ips(digits: str, digits_size: int = -1, start: int = 0, octet_num: int = 1) -> List[str]:
    if digits_size < 0:
        digits_size = len(digits)

    _ips = []
    for octet_value, octet_len in octet_permutations(digits[start:start + 3], octet_num):
        if octet_num == 4 and start + octet_len == digits_size:
            _ips.append(octet_value)
        else:
            _ips.extend([f'{octet_value}.{rest_of_ip}' for rest_of_ip in ips(digits, digits_size, start + octet_len, octet_num + 1)])
    else:
        return sorted(_ips)


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
assert ips('1231231231231') == []

# acceptance cases
assert ips('2542540123') == ['254.25.40.123', '254.254.0.123']
assert ips('25525511135') == ['255.255.11.135', '255.255.111.35']
assert ips('11111011111') == ['111.110.11.111', '111.110.111.11']
assert ips('25505011535') == []
