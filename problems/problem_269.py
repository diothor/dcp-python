def push_dominoes_simple(dominoes: str) -> str:
    out = ''
    left_border = 'L'
    count = 0
    for d in dominoes + 'R':
        if d == '.':
            count += 1
        elif d in ('L', 'R'):
            right_border = d
            if right_border == left_border:
                out += right_border * count
            elif left_border == 'L' and right_border == 'R':
                out += '.' * count
            else:  # left_border == 'R' and right_border == 'L'
                side = count // 2
                out += left_border * side + ('.' if count % 2 == 1 else '') + right_border * side
            out += right_border
            left_border = right_border
            count = 0
        else:
            out += d

    return out[:-1]


def push_dominoes_elegant(dominoes: str) -> str:
    edges = [(-1, 'L')] + [(i, d) for i, d in enumerate(dominoes) if d in ('L', 'R')] + [(len(dominoes), 'R')]
    sections = zip(edges, edges[1:])
    out = list(dominoes)

    for (start, ledge), (end, redge) in sections:
        start += 1
        if ledge == redge:
            out[start:end] = ledge * (end - start)
        elif ledge == 'R' and redge == 'L':
            side = (end - start) // 2
            out[start:start + side] = ledge * side
            out[end - side:end] = redge * side

    return ''.join(out)


def push_dominoes_force(dominoes: str) -> str:
    # creating list of force values for each domino piece. The default value 0.
    force_values = [0] * len(dominoes)
    max_force = len(dominoes)

    # going left -> right; applying force directed right (positive values)
    force = 0
    for i, d in enumerate(dominoes):
        if d == 'R':
            force = max_force
        if d == 'L':
            force = 0
        force_values[i] += max(force, 0)
        force -= 1

    # going right -> left; applying force directed left (negative values)
    force = 0
    for i in range(max_force - 1, -1, -1):
        d = dominoes[i]
        if d == 'L':
            force = max_force
        if d == 'R':
            force = 0
        force_values[i] -= max(force, 0)
        force -= 1

    # Pick how domino piece looks like based on force value. DOT if 0, L if negative, R if positive.
    return ''.join(['.LR'[(0 > o) - (0 < o)] for o in force_values])
