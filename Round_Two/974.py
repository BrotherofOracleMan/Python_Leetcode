class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p_sum = 0
        hash_table = defaultdict(int)
        hash_table[0] = 1
        ans = 0
        for i in range(len(nums)):
            p_sum += nums[i]
            p_sum %= k
            if p_sum in hash_table:
                ans += hash_table[p_sum]
            hash_table[p_sum] +=1
        return ans
