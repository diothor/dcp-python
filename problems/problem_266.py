from my_decors import timeit
from collections import Counter


def load_dict(path):
    return [word.strip().lower() for word in open(path, 'r', encoding='UTF8').readlines()]


@timeit
def step_words(word, dictionary):
    w_size = len(word)
    letters = Counter(word)
    steps = [entry for entry in dictionary if len(entry) == w_size + 1 if len(letters - Counter(entry)) == 0]
    steps.sort()
    return steps


en_dict = load_dict('data/engmix.txt')
similar = step_words('apple', en_dict)
print(f'{len(similar)} found: {similar}')
assert 'appeal' in similar
