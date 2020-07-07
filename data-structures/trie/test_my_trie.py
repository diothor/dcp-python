from trie.my_trie import MyTrie


def test():
    trie = MyTrie()
    trie.insert('abcdef')
    trie.insert('baba')
    trie.insert('ban')
    assert trie.search('abcde') is False
    assert trie.search('abcdef') is True
    assert trie.search('ban') is True
