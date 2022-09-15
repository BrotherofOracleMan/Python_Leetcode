class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        DP = (n+1) * [0]
        DP[1] = 1
        DP[2] = 2
        for i in range(3,n+1,1):
            DP[i] = DP[i-1] + DP[i-2]
        print(DP)
        return DP[n]
            
