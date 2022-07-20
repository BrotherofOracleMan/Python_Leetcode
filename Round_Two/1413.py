class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min_val = 0
        tempsum = 0
        for i in range(len(nums)):
            tempsum +=nums[i]
            min_val = min(tempsum, min_val)
        
        
        return -min_val + 1
        """
        min_start = 1
        max_start = abs(sum(nums)-nums[0])
        temp_sum = 0
        print(max_start)
        while min_start:
            temp_sum = min_start
            for i in range(0, len(nums)):
                temp_sum += nums[i]
                if temp_sum < 1:
                    break
                if i == len(nums) - 1:
                    return min_start
            min_start +=1
        return min_start
        """
        
