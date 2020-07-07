class TrieNode:
    def __init__(self, end_word: bool = False):
        self.children = {}
        self.end_word = end_word

    def __repr__(self):
        return ','.join(sorted(self.children.keys()))


class MyTrie:
    def __init__(self):
        self.root = TrieNode()

    # O(n) where n is number of letters in word. It's equal to len(word).
    def insert(self, word: str):
        node = self.root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        else:
            node.end_word = True

    # O(n) where n is number of letters in word. It's equal to len(word).
    def search(self, word) -> bool:
        node = self.root
        for letter in word:
            node = node.children.get(letter)  # O(1) cause of hashing in TrieNode::children as this property is a dictionary
            if node is None:
                return False
        else:
            return node.end_word
