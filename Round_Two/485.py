class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j, i = 0,0
        max_ones = 0
        while j < len(nums):
            if nums[j] == 0 or nums[i] == 0:
                i = j
            if nums[j] == 1 or nums[i] == 1:
                max_ones = max(j-i+1,max_ones)
            j+=1
        return max_ones
