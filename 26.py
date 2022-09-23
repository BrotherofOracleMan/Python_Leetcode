class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_ptr = 0
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                left_ptr +=1
                nums[left_ptr] = nums[r]

        return left_ptr+1
