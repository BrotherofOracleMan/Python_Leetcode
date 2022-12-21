class TrieNode():
    def __init__(self,char) -> None:
        self.character = char
        self.children = {}
        self.endofword = False

class Trie:

    def __init__(self):
        self.root = TrieNode("")
        return

    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode(character)
                node = node.children[character]
            else:
                node = node.children[character]
        node.endofword = True
        return

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(string, root):
            if len(string) == 0:
                return root.endofword
            if string[0] not in root.children:
                return False
            else:
                return dfs(string[1:],root.children[string[0]])
        return dfs(word, node)

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        def dfs(word, root):
            if word == "":
                return True
            if word[0] not in root.children:
                return False
            else:
                return dfs(word[1:],root.children[word[0]])
        return dfs(prefix,node)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
