class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_0s = 0
        num_1s =  0
        num_2s = 0
        
        for i in nums:
            if i is 0:
                num_0s +=1
            elif i is 1:
                num_1s  +=1
            elif i is 2:
                num_2s  +=1
                
        for i in range(len(nums)):
            if num_0s > 0:
                nums[i] = 0
                num_0s-=1
            elif num_1s > 0:
                nums[i] = 1
                num_1s-=1
            elif num_2s > 0:
                nums[i] = 2
                num_2s-=1
        return 
