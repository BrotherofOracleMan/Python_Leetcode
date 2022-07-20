class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num_sum = 0
        leftSum = 0
        n = len(nums)
        pivot_index = -1
        for i in range(n):
            num_sum += nums[i]
            
        for i in range(n):
            if leftSum == num_sum - leftSum - nums[i]:
                return i
            leftSum += nums[i]

        return -1
