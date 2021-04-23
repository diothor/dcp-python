from typing import Dict, List
from collections import deque


# O(P+R) where P is number of people (the keys) and R is length of union of all friend lists (the values) in friendship
def count_groups(friendships: Dict[int, List[int]]) -> int:
    groups = 0
    ppl = set(friendships.keys())
    visited = set()
    while ppl:
        groups += 1
        ppl_in_group = deque()
        ppl_in_group.append(ppl.pop())
        while ppl_in_group:  # O(P) where P is number of people
            person = ppl_in_group.pop()
            if person not in visited:
                visited.add(person)  # O(1)
                ppl.discard(person)  # O(1)
                ppl_in_group.extendleft(friendships[person])  # O(R) is number of relations of the person
    else:
        return groups


# no people in class
assert count_groups({}) == 0

# all ppl in a single group
people = {
    0: [1, 2],
    1: [3, 4],
    2: [3],
    3: [4],
    4: [1]
}
assert count_groups(people) == 1

# acceptance case
people = {
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}
assert count_groups(people) == 3
