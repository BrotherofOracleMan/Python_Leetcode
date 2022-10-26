class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = [0] * 26
        if len(s) != len(t):
            return False

        for s_it in s:
            s_hash[ord(s_it) - ord('a') ] += 1
        
        for t_it in t:
            s_hash[ord(t_it) - ord('a')] -=1
            if(s_hash[ord(t_it) - ord('a')] < 0):
                return False

        return True
