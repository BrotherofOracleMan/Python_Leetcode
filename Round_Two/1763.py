class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_nice(s):
            return len(set(s.lower())) == (len(set(s))//2)
        
        window_size = len(s)
        
        while window_size:
            for j in range(0,len(s)-window_size +1):
                if get_nice(s[j:j+window_size]):
                    return s[j:j+window_size]
            window_size -=1
        return ""
