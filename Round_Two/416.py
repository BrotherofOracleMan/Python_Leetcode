class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n_sum = sum(nums)
        if n_sum%2 == 1:
            return False
        subsetSum = n_sum//2
        n = len(nums)
        dp = [[False] * (subsetSum+1) for _ in range(0,n +1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(0, subsetSum + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
        return dp[n][subsetSum]
