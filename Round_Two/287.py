class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        hare = nums[0]

        while hare != tortoise:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
        """
        low = 1
        high = len(nums) -1
        while low <= high:
            mid = low + (high - low)//2
            count = sum(num <= mid for num in nums)
            if count > mid:
                duplicate = mid
                high = mid - 1
            else:
                low = mid +1

        return duplicate
        """
