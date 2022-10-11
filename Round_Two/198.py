class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxDP = [0] * len(nums)
        maxDP[0] = nums[0]
        maxDP[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            maxDP[i] = max(maxDP[i-1],maxDP[i-2] + nums[i])
        return maxDP[-1]
