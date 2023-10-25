class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        list1 = [0] * 26
        ans = []
        for i in range(0, len(words[0])):
            list1[ord(words[0][i]) - ord('a')] +=1
        
        for i in range(1, len(words)):
            list2 = [0] * 26
            for j in range(0, len(words[i])):
                list2[ord(words[i][j]) - ord('a')] +=1
            for z in range(0,26):
                list1[z] = min(list1[z], list2[z])
        
        for i in range(0, 26):
            if list1[i] !=0:
                ans += [chr(ord('a') + i)] * list1[i]
        return ans
