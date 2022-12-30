class TrieNode():
    def __init__(self,char) -> None:
        self.charactar = char
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
                node = node.children[char]
            else:
                node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def search_helper(word, node):
            if node is None:
                return False
            if word == "":
                return node.endOfWord
            if word[0] != ".":
                return search_helper(word[1:],node.children.get(word[0]))
            else:
                for trienode in node.children:
                    if search_helper(word[1:],node.children.get(trienode)):
                        return True
        return search_helper(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
