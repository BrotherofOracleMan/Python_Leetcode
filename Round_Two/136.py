class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNum = nums[0]
        for i in range(1, len(nums)):
            singleNum = singleNum ^ nums[i]
        return singleNum
