class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        DP=[float("inf")] * n
        DP[0] = 0
        if n == 1:
            return 0

        for start_poisition in range(n):
            for addition in range(1, nums[start_poisition] + 1):
                if start_poisition + addition < n:
                    DP[start_poisition + addition] = min(DP[start_poisition + addition], DP[start_poisition] + 1)
        return DP[n-1]
