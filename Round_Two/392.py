class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s) + 1
        m = len(t) + 1
        DP = [ [0]*m for x in range(0,n)]
        
        for row in range(1,n):
            for col in range(1,m):
                if s[row -1 ] == t[col -1]:
                    DP[row][col] = 1 + DP[row-1][col-1]
                else:
                    DP[row][col] = max(DP[row][col-1],DP[row-1][col])
        return DP[n-1][m-1] == len(s)
        
