import logging
import string

from nltk import SyllableTokenizer, word_tokenize
from termcolor import colored

logging.basicConfig(level='DEBUG')
f = open('data/pomidor.txt', encoding='UTF8')
colours = ('blue', 'red')
counter = 0
sonority_hierarchy = [
    "aeiouyąę",  # vowels.
    "lłmnw",  # nasals.
    "zvsfźżśŻ",  # fricatives.
    "brcdgtkpqxhj",  # stops.
]
ssp = SyllableTokenizer(sonority_hierarchy=sonority_hierarchy)
output = ''
for line in f.readlines():
    chunks = word_tokenize(line, 'polish')
    logging.debug('chunks: %s', chunks)
    new_line = ''
    for chunk in chunks:
        if chunk not in string.punctuation:
            new_line += ' '
        else:
            new_line += colored(chunk, colours[(counter - 1) % 2])
            continue

        if len(chunk) < 2:
            new_line += colored(chunk, colours[0])
            continue

        syllables = ssp.tokenize(chunk)
        for syll in syllables:
            new_line += colored(syll, colours[counter % 2])
            counter += 1
    output += new_line.strip() + '\n'

print(output.strip())
