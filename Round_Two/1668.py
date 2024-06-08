class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_val = 0
        for i in range(len(sequence) - len(word)+1):
            if sequence[i:i + len(word)] == word:
                k = 0
                index = i
                print(index)
                while index <= len(sequence) - len(word):
                    if sequence[index: index + len(word)] == word:
                        k += 1
                    else:
                        break
                    index += len(word)
                max_val = max(max_val, k)
        return max_val
