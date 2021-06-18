class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        _sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == _sum - nums[i]- left_sum:
                return i
            left_sum +=nums[i]
        
        return -1
