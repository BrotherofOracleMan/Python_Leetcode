class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        longest_value = 0
        
        for index,value in enumerate(nums):
            if index and nums[index-1] >= nums[index]:
                start = index
            longest_value = max(index-start+1,longest_value)
        return longest_value
            
        
