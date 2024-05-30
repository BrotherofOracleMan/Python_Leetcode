class Solution:
    def startswith(self, word_i, word_j):
        return word_i == word_j[:len(word_i)] if len(word_i) <= len(word_j) else False

    def endswith(self, word_i, word_j):
        return word_i == word_j[-len(word_i):] if len(word_i) <= len(word_j) else False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for j_ind in range(1, len(words)):
            for i_ind in range(j_ind):
                if self.startswith(words[i_ind], words[j_ind]) and self.endswith(words[i_ind], words[j_ind]):
                    ans += 1
        return ans
