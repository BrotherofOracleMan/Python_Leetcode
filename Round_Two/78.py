class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def backtrackhelper(length,arr,index):
            if index == length:
                return 
            for i in range(index,length):
                arr.append(nums[i])
                ans.append(list(arr))
                backtrackhelper(length,arr,i+1)
                arr.pop()
        backtrackhelper(len(nums),[] ,0)
        return ans