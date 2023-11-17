class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h_t = [0] * 26

        for c in s:
            h_t[ord(c) - ord('a')] +=1
        
        for index, c in enumerate(s):
            if h_t[ord(c) - ord('a')] == 1:
                return index
        return -1 
