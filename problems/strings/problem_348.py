class TernaryTreeNode:
    def __init__(self, letter):
        self.letter = letter
        self.end_word = False
        self.tree_lower = None
        self.tree_equal = None
        self.tree_higher = None

    def __str__(self):
        return f'{self.letter}: [{self.tree_lower}, {self.tree_equal}, {self.tree_higher}]'


class TernarySearchTree:
    def __init__(self):
        self.root = None
        pass

    def insert(self, word):
        self.root = self.__insert(word, self.root, 0)

    def __insert(self, word: str, curr_node: TernaryTreeNode or None, letter) -> TernaryTreeNode:
        if curr_node is None:
            curr_node = TernaryTreeNode(word[letter])

        if curr_node.letter > word[letter]:
            curr_node.tree_lower = self.__insert(word, curr_node.tree_lower, letter)
        elif curr_node.letter < word[letter]:
            curr_node.tree_higher = self.__insert(word, curr_node.tree_higher, letter)
        elif letter + 1 < len(word):
            curr_node.tree_equal = self.__insert(word, curr_node.tree_equal, letter + 1)
        else:
            curr_node.end_word = True

        return curr_node

    def search(self, word) -> bool:
        node = self.root
        letter = 0
        while letter < len(word):
            if node is None:
                return False
            elif node.letter > word[letter]:
                node = node.tree_lower
            elif node.letter < word[letter]:
                node = node.tree_higher
            elif letter + 1 < len(word):
                node = node.tree_equal
                letter += 1
            else:
                return node.end_word
        else:
            return False

    def traverse(self):
        res = self.__traverse(self.root)
        return res

    def __traverse(self, node: TernaryTreeNode) -> list:
        res = []
        if node is not None:
            res.append(node.letter + '*' * node.end_word)
            res += self.__traverse(node.tree_lower)
            res += self.__traverse(node.tree_equal)
            res += self.__traverse(node.tree_higher)
        return res


tree = TernarySearchTree()
assert tree.traverse() == []
assert tree.search('aaa') is False
tree.insert('code')
assert tree.traverse() == ['c', 'o', 'd', 'e*']
tree.insert('codewars')
assert tree.traverse() == ['c', 'o', 'd', 'e*', 'w', 'a', 'r', 's*']
tree.insert('cob')
assert tree.traverse() == ['c', 'o', 'd', 'b*', 'e*', 'w', 'a', 'r', 's*']
tree.insert('cobol')
assert tree.traverse() == ['c', 'o', 'd', 'b*', 'o', 'l*', 'e*', 'w', 'a', 'r', 's*']
tree.insert('cobo')
assert tree.traverse() == ['c', 'o', 'd', 'b*', 'o*', 'l*', 'e*', 'w', 'a', 'r', 's*']
assert tree.search('cobo') is True

tree = TernarySearchTree()
tree.insert('code')
tree.insert('cob')
tree.insert('be')
tree.insert('ax')
tree.insert('war')
tree.insert('we')
assert tree.search('code') is True
assert tree.search('cob') is True
assert tree.search('cod') is False
assert tree.search('war') is True
assert tree.search('wr') is False
