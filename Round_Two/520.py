class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        num_capitals = 0
        for c in word:
            if c.isupper():
                num_capitals +=1
        return num_capitals == len(word) or (num_capitals == 1 and word[0].isupper()) or num_capitals == 0 
        
