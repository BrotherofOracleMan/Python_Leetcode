class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1] * len(nums)

        for end in range(1, len(nums)):
            for start in range(end):
                if nums[end] > nums[start]:
                    DP[end] = max(DP[end], DP[start] + 1)
        return max(DP)
