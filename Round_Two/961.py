from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hset = set()

        for num in nums:
            if num in hset:
                return num
            else:
                hset.add(num)

        """
        ans_len = len(nums)//2
        ht = defaultdict(int)

        for num in nums:
            ht[num] += 1
            if ht[num] == ans_len:
                return num
        """
