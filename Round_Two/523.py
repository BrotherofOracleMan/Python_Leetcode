class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        p_sum = 0
        hash_map[0] = -1
        
        
        for i in range(len(nums)):
            p_sum += nums[i]
            p_sum = p_sum %k
            if p_sum in hash_map:
                if i - hash_map[p_sum] >= 2:
                    return True
            if p_sum not in hash_map:
                hash_map[p_sum] = i
        return False
