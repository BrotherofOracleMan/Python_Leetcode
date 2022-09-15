class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        min_cost = 0
        n = len(cost)
        
        if n <= 2:
            return min(cost[0] , cost[1])
        
        
        DP = (n+1) * [0]
        DP[0] = cost[0]
        DP[1] = cost[1]
        
        for i in range(2, n,1):
            DP[i] = cost[i] + min(DP[i-1],DP[i-2])
        DP[n] = min(DP[n-1],DP[n-2])
        return DP[n]
        
