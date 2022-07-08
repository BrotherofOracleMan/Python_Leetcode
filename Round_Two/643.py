class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        temp_sum, max_average = 0,float('-inf')

        
        for j in range(len(nums)):
            temp_sum += nums[j]
            if ((j-i) + 1 > k):
                temp_sum -= nums[i]
                i += 1
            if ((j-i+1)  == k):
                max_average = max(max_average, temp_sum)
        return float(max_average)/float(k)
        



"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        temp_sum, max_average = 0,float('-inf')
        
        for i in range(k):
            temp_sum += nums[i]
        max_average = temp_sum
        for j in range(k,len(nums)):
            print(j)
            temp_sum += nums[j] - nums[j-k]
            max_average = max(temp_sum,max_average)
        return float(max_average)/float(k)
        
"""
