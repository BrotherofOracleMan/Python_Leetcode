class Solution:
    def compareWord(self, word1, word2, comp_d):
        if len(word1) > len(word2) and word2 == word1[0:len(word2)]:
            return False

        N = min(len(word1), len(word2))
        for i in range(N):
            if word1[i] == word2[i]:
                continue
            elif comp_d[word1[i]] < comp_d[word2[i]]:
                return True
            elif comp_d[word1[i]] > comp_d[word2[i]]:
                return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        comp_d = {}
        for index, c in enumerate(order):
            comp_d[c] = index

        for i in range(len(words) - 1):
            if not self.compareWord(words[i], words[i+1], comp_d):
                return False
        return True
