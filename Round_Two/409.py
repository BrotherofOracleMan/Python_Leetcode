from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        h_t = defaultdict(int)
        num = 0
        ans = 0
        for char in s:
            h_t[char] += 1
        
        for key in h_t.keys():
            ans +=(h_t[key]//2) * 2
            if ans %2 == 0 and h_t[key] %2 == 1:
                ans +=1
        return ans
