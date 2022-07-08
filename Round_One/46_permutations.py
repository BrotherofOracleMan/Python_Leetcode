class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def permutation_helper(nums,nums_list,left,k):
            if left == k:
                nums_list.append(nums[:])
                return

            for i in range(left,k):
                print(left)
                nums[left],nums[i] = nums[i],nums[left]
                permutation_helper(nums,nums_list,left+1,k)
                nums[left],nums[i] = nums[i],nums[left]
        
        nums_list = []
        permutation_helper(nums,nums_list,0,len(nums))
        
        return nums_list

            
        
