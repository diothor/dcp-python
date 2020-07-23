from typing import Union


# O(nlogn)
def h_index(*papers) -> Union[int, None]:
    sorted_papers = sorted(papers, reverse=True)
    for papers_quoted_as_much, num_of_quotes in enumerate(sorted_papers):
        if num_of_quotes <= papers_quoted_as_much + 1:  # +1 cause the indexing starts at 0 and this is sort of not counting current element
            return num_of_quotes
    else:
        return None


assert h_index() is None
assert h_index(0) == 0
assert h_index(1) == 1
assert h_index(2) is None

assert h_index(3, 3) is None
assert h_index(3, 3, 3) == 3

assert h_index(1, 2, 3, 4, 5, 6) == 3
assert h_index(4, 0, 0, 2, 3) == 2
