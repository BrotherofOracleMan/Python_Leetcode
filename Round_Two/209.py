class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        current_sum  = 0
        i = 0
        min_result = len(nums) + 2
        
        for j in range(len(nums)):
            current_sum +=nums[j]
            while i <= j and current_sum >= target:
                min_result = min(min_result,j-i+1)
                current_sum -= nums[i]
                i+=1
        return min_result if min_result != (len(nums) + 2) else 0
