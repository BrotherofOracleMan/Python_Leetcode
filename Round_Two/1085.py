class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        num_sum = 0
        while min_num > 0:
            num_sum += min_num %10
            min_num = min_num // 10
        return 1 if num_sum%2 == 0 else 0
        
