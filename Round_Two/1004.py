class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_sliding_window = 0
        number_of_zeros  = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k-=1
            if k < 0:
                if nums[i] == 0:
                    k+=1
                i+=1
        return j-i+1

"""
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_sliding_window = 0
        number_of_zeros  = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                number_of_zeros +=1
            while number_of_zeros > k:
                if nums[i] == 0:
                    number_of_zeros -=1
                i+=1
            max_sliding_window = max(max_sliding_window,j - i +1)
        return max_sliding_window
"""
