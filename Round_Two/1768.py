class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        word1_ptr , word2_ptr = 0,0
        result = ""

        while word1_ptr < len_word1 or word2_ptr < len_word2:
            if word1_ptr < len_word1:
                result += word1[word1_ptr]
                word1_ptr +=1

            if word2_ptr < len_word2:
                result += word2[word2_ptr]
                word2_ptr +=1
        return result
        
