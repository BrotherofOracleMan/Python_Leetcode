class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        sol = []
        size = len(nums) - 1

        if len(nums) == 0:
            return [[lower, upper]]

        if lower < nums[0]:
            sol.append([lower, nums[0] - 1])
        
        for i in range(0, size):
            first_num = nums[i]
            second_num = nums[i + 1]
            if first_num != second_num - 1:
                sol.append([first_num + 1, second_num - 1])
        
        if upper > nums[-1]:
            sol.append([nums[-1] + 1, upper])

        return sol
