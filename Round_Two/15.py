class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i-1]:
                self.threeSum_helper(i,nums,ans)
        return ans
            
    def threeSum_helper(self,i,nums,ans):
        low = i +1
        high = len(nums) -1
        while low < high:
            num_sum = nums[i] + nums[low] + nums[high]
            if num_sum < 0:
                low += 1
            elif num_sum > 0:
                high -=1
            else:
                ans.append([nums[i],nums[low],nums[high]])
                low +=1
                high -=1
                while nums[low] == nums[low-1] and low < high:
                    low +=1
