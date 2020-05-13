# I came up with the "__find_node" abstraction, which I think really worked
# for all the necessary cases

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ends_word = False
        self.branches = {} # char->trie

    def __find_node(self, word, i, create):
        if i == len(word):
            return self
        if word[i] in self.branches:
            return self.branches[word[i]].__find_node(word, i+1, create)
        if create:
            node = Trie()
            self.branches[word[i]] = node
            return node.__find_node(word, i+1, create)
        return None


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.__find_node(word, 0, True)
        node.ends_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.__find_node(word, 0, False)
        return node != None and node.ends_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.__find_node(prefix, 0, False)
        return node != None
