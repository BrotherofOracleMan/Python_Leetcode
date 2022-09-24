class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curr_min = nums[0]
        curr_max = nums[0]
        ans = curr_max
        tmp_max = curr_max
        
        for num in nums[1:]:
            curr_max = max(num, curr_min * num, tmp_max * num)
            curr_min = min(num, curr_min * num, tmp_max * num)

            tmp_max = curr_max
            ans = max(ans, curr_max)
        
        return ans
