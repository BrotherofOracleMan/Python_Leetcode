class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) + 1
        m = len(text2) + 1
        DP = [[0]* m for i in range(n)]

        for row in range(1,n):
            for col in range(1,m):
                if text1[row-1] == text2[col-1]:
                    DP[row][col] = 1 + DP[row-1][col-1]
                else:
                    DP[row][col] = max(DP[row][col-1],DP[row-1][col])
        return DP[n-1][m-1] 
