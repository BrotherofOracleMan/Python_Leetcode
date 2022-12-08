class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_highest_target():
            low = 0
            high = len(nums) -1
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] <= target:
                    low = mid + 1 
                else:
                    high = mid-1
            return high 
        
        def find_lowest_target():
            low = 0
            high = len(nums) -1
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] < target:
                    low = mid + 1 
                else:
                    high = mid-1
            return low
        high = find_highest_target()
        low = find_lowest_target()
        if low >= 0 and low < len(nums) and low <= high and nums[low] == target:
            return[low,high] 
        else:
            return [-1,-1]
        return[find_lowest_target(),find_highest_target()]
