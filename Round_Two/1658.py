class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        current_sum = 0
        total_sum = sum(nums)
        max_indice = -1
        for j in range(0, len(nums)):
            current_sum += nums[j]
            while i <= j and current_sum > total_sum -x:
                current_sum  -= nums[i]
                i+=1
            if current_sum == total_sum - x:
                max_indice = max(max_indice, j - i +1)
        return n - max_indice if max_indice != -1 else -1
