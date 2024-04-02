class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        current_max = -1
        current_min = float("inf")
        for fast_ptr in range(len(nums)):
            if nums[fast_ptr] - current_min > current_max and nums[fast_ptr] > current_min:
                current_max = max(current_max, nums[fast_ptr] - current_min)
            current_min = min(current_min, nums[fast_ptr])
        return current_max
