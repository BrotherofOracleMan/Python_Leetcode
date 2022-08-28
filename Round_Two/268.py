class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_sum = (len(nums) * (len(nums) +1))//2
        for i in nums:
            num_sum -= i
        return num_sum
        
