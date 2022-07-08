class Solution:
    def findUnsortedSubarray(self, nums):
        stack = []
        start , end = len(nums) -1 , 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                num = stack.pop()
                start = min(num,start)
            stack.append(i)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                num = stack.pop()
                end = max(num,end)
            stack.append(i)
        return end - start + 1 if end - start > 0 else 0
