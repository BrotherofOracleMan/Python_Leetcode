class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsets_helper(nums,subset,subsets,left,k):
            if len(subset) == k:
                subsets.append(list(subset))
                return
            for i in range(left,len(nums)):
                subset.append(nums[i])
                subsets_helper(nums,subset,subsets,i+1,k)
                subset.pop()
        
        subsets = []
        for i in range(len(nums)+1):
            subsets_helper(nums,[],subsets,0,i)
        return subsets
