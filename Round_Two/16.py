class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        lowest_target_value = float('inf')
        for index in range(len(nums)):
            low = index + 1
            high = len(nums) - 1
            while low < high:
                num_sum = nums[index] + nums[low] + nums[high]
                if abs(target - num_sum) < abs(lowest_target_value):
                    lowest_target_value = abs(target - num_sum)
                    ans = num_sum
                if num_sum < target:
                    low+=1
                else:
                    high -= 1
                if abs(target - num_sum) == 0:
                    break
        return ans
