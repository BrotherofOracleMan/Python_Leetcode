class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 1

        while pivot >= 1 and nums[pivot] <= nums[pivot-1]:
            pivot -= 1

        if pivot != 0:
            i = len(nums) - 1
            while nums[i] <= nums[pivot -1]:
                i -= 1
            nums[pivot -1] , nums[i] = nums[i], nums[pivot - 1]
        left = pivot
        right = len(nums) - 1

        while left < right:
            nums[left] , nums[right] = nums[right], nums[left]
            left +=1
            right -=1



