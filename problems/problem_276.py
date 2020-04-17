def search_naive(text: str, pattern: str):
    if len(pattern) == 0:
        return []

    ts = len(text)
    ps = len(pattern)

    found = []
    for i in range(ts - ps + 1):
        for j in range(ps):
            if text[i + j] != pattern[j]:
                break
        else:
            found.append(i)
    return found


def search_kmp(text: str, pattern: str):
    if len(pattern) == 0:
        return []

    lps = longest_proper_prefixes(pattern)
    found = []
    ts = len(text)
    ps = len(pattern)
    ti = 0
    pi = 0

    while ti < ts:
        if text[ti] == pattern[pi]:
            ti += 1
            pi += 1

            if pi == ps:
                found.append(ti - pi)
                pi = lps[-1]
        elif pi == 0:
            ti += 1
        else:
            pi = lps[pi - 1]

    return found


def longest_proper_prefixes(s: str) -> list:
    lsp = [0] * len(s)

    i = 1
    pref_size = 0
    while i < len(s):
        if s[pref_size] == s[i]:
            pref_size += 1
        elif pref_size > 0:
            pref_size -= 1
            continue
        else:
            # perf_size is 0;
            pass

        lsp[i] = pref_size
        i += 1

    return lsp
