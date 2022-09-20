class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num_sum = 0
        max_sum = float('-inf')
        
        for num in nums:
            num_sum = max(num_sum + num , num)
            max_sum = max(num_sum, max_sum)
        
        return max_sum
        
