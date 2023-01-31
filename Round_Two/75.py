class Solution:
    def sortColors(self, nums: List[int]) -> None:
        b_ptr = curr =0
        e_ptr = len(nums) -1

        while curr <= e_ptr:
            if nums[curr] == 0:
                nums[curr], nums[b_ptr] = nums[b_ptr], nums[curr]
                b_ptr +=1
                curr +=1
            elif nums[curr] == 2:
                nums[curr], nums[e_ptr] = nums[e_ptr], nums[curr]
                e_ptr-=1
            else:
                curr +=1
