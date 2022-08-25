class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash_set = dict()
        ans = [0,0]
        for i,num in enumerate(nums):
            if target - num in nums_hash_set and i != nums_hash_set[target-num] :
                ans[0] = i
                ans[1] = nums_hash_set[target - num]
                return ans
            nums_hash_set[num] = i 
        return ans
        
