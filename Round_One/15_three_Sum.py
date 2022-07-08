class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def threeSumHelper(nums,start, sol):
            low, high = start + 1, len(nums) - 1
            while low < high:
                if nums[start] + nums[low] + nums[high] == 0:
                    sol.append([nums[i], nums[low], nums[high]])
                    #avoid duplicates here
                    low+=1
                    high -=1
                    while low < high and nums[low] == nums[low -1]:
                        low+=1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    low += 1
        
        nums.sort()
        sol = []
        
        for i in range(len(nums)):
            if nums[i] >0:
                #indicator that all values are positive so impossible to get tto zero
                break
            if i == 0 or nums[i-1] != nums[i]:
                threeSumHelper(nums,i,sol)
        
        
        return sol
                
