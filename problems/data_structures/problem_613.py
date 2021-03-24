from __future__ import annotations
from typing import Optional, Dict


class TrieNode:

    def __init__(self):
        self.letters: Dict[str, TrieNode] = {}
        self.value: Optional[int] = None

    def end_of_word(self) -> bool:
        return self.value is not None

    def get_value(self) -> int:
        return 0 if self.value is None else self.value

    def insert(self, word: str, value: int = 0, iletter: int = 0, length: int = -1) -> None:
        if length < 0:
            length = len(word)
        elif iletter == length:
            self.value = value
            return

        letter = word[iletter]
        self.letters.setdefault(letter, TrieNode()).insert(word, value, iletter + 1, length)
        return

    def prefix(self, word, iletter: int = 0, length: int = -1) -> Optional[TrieNode]:
        if length < 0:
            length = len(word)
        elif iletter == length:
            return self

        letter = word[iletter]
        return None if letter not in self.letters else self.letters[letter].prefix(word, iletter + 1, length)


trie = TrieNode()
trie.insert('abcde')
assert trie.prefix('abcde')
assert not trie.prefix('abcdef')
assert trie.prefix('abcd')

trie.insert('abgh')
assert trie.prefix('abg')
assert not trie.prefix('abgd')


class PrefixMaxSum:

    def __init__(self):
        self.trie = TrieNode()

    # O(n) where n is number of letters in key
    def insert(self, key: str, value: int) -> PrefixMaxSum:
        self.trie.insert(key, value)
        return self

    def _trie_sum(self, trie_node: TrieNode) -> int:
        node_sum = trie_node.get_value()
        for sub_node in trie_node.letters.values():
            node_sum += self._trie_sum(sub_node)
        return node_sum

    # O(l + n) where l is length of prefix and n is number of all unique letters in keys starting with prefix
    def sum(self, prefix: str) -> int:
        prefix_node = self.trie.prefix(prefix)  # O(l)
        return 0 if not prefix_node else self._trie_sum(prefix_node)  # O(n)


mapsum = PrefixMaxSum()
mapsum.insert('a', 1)
assert mapsum.sum('a') == 1
mapsum.insert('a', 2)
assert mapsum.sum('a') == 2

mapsum.insert('ab', 7)
assert mapsum.sum('a') == 9

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3
mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
