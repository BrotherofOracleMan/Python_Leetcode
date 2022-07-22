class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n_sum =0 
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        num_subarrays = 0
        
        for i in range(len(nums)):
            n_sum += nums[i]
            if n_sum -k in prefix_sum:
                num_subarrays += prefix_sum[n_sum-k]
            
            prefix_sum[n_sum] += 1
        return num_subarrays
