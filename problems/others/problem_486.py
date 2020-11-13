from typing import List, Union


class Crowd:

    def __init__(self, matrix: List[List[int]]):
        self.relations = matrix

    def __knows(self, a: int, b: int) -> bool:
        return self.relations[a][b] == 1

    # O(n)
    def celebrity(self) -> Union[int, None]:
        ppl = [p for p in range(len(self.relations))]  # O(n)
        while len(ppl) > 1:  # O(n)
            a, b = ppl.pop(), ppl.pop()
            ppl.append(b if self.__knows(a, b) else a)
        else:
            celebrity = ppl.pop()

        if sum(self.relations[celebrity]) > 0:  # O(n)
            # celebrity shouldn't know anybody
            return None
        elif not all([row[celebrity] for i, row in enumerate(self.relations) if i != celebrity]):  # O(n)
            # everybody should know the celebrity
            return None
        else:
            return celebrity


guests = Crowd([
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
])
assert guests.celebrity() == 2

guests = Crowd([
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
])
assert guests.celebrity() is None

guests = Crowd([
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
])
assert guests.celebrity() is None
