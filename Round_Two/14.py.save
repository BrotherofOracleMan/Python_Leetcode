class Solution:
    def get_index_between_two_words(self,word1,word2):
        length = min(len(word1), len(word2))
        index = 0
        for i in range(length):
            if word1[i] != word2[i]:
                return i
        return length

    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = len(strs[0])
        comparison_word = strs[0]
            
        for word in strs[1:]:
            index = self.get_index_between_two_words(comparison_word, word)
            answer = min(index,answer)

        return strs[0][:answer]
