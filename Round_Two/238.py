class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        """
        left = [0] * len(nums)
        right = [0] * len(nums)
        answer = [0] * len(nums)
        left[0] = 1
        right[-1] = 1
        
        for i in range(1 , len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
            
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        return answer
        """
        
        answer = [0] * len(nums)
        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        R = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
