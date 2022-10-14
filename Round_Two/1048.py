class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        max_word_chain = 1
        DP = dict()
        words.sort(key=len)
        for word in words:
            max_current_word_length = 1
            for i in range(len(word)):
                old_word = word[:i] + word[i+1:]
                length = DP[old_word] if old_word in DP else 0
                max_current_word_length = max(1+length,max_current_word_length)
            DP[word] = max_current_word_length
            max_word_chain = max(max_word_chain,max_current_word_length)
        return max_word_chain
