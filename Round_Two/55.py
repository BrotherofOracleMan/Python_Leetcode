class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        DP = [False] * n
        DP[0] = True
        if n == 1:
            return True
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if DP[j] == True and nums[j] + j >= i:
                    DP[i] = True
                    break
        return DP[-1]
