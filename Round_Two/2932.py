class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    ans = max(nums[i] ^ nums[j], ans)
        return ans 
