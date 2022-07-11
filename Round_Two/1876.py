class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_string = 0
        
        for j in range(0,len(s) - 2):
            hash_set = set(s[j:j+3])
            if len(hash_set) == 3:
                num_string +=1
        return num_string
