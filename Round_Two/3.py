class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        hash_table = defaultdict(int)
        max_sliding_window = 0
        
        for j in range(len(s)):
            while hash_table[s[j]]:
                hash_table[s[i]] -=1
                i+=1
            max_sliding_window = max(max_sliding_window, j-i+1)
            hash_table[s[j]]+=1
        return max_sliding_window
                
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        hash_set = set()
        max_sliding_window = 0
        
        for j in range(len(s)):
            while s[j] in hash_set:
                hash_set.remove(s[i])
                i+=1
            max_sliding_window = max(max_sliding_window, j-i+1)
            hash_set.add(s[j])
        return max_sliding_window
                

"""
