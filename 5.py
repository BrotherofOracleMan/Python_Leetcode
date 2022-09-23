class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        DP = [[False] * n for _ in range(0,n)]
        
        for i in range(n):
            DP[i][i] = True
        
        maxlen = 1
        starting_index = 0
        for end in range(0,n):
            for start in range(end-1, -1, -1):
                if s[end] == s[start]:
                    if end - start == 1 or DP[start+1][end-1]:
                        DP[start][end] = True
                        palindrome_size = end-start+1
                        if palindrome_size > maxlen:
                            maxlen = palindrome_size
                            starting_index = start
        return s[starting_index : starting_index + maxlen]
        
