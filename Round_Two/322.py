class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        DP = [float('inf')]  * (n +1)
        DP[0] = 0
        print(DP)
        for coin in coins:
            for j in range(coin, n + 1):
                DP[j] = min(DP[j], DP[j-coin]+1)
        return DP[n] if DP[n] != float('inf') else -1
"""
Top down solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [float('inf')]  * (amount +1)
        DP[0] = 0
        n = len(coins)
        
        def coin_helper(n_amount):
            
            if n_amount < 0:
                return math.inf
            if n_amount == 0:
                return 0
            if n_amount in DP:
                return DP[n_amount]
            
            for j in range(n):
                    DP[n_amount] = min(coin_helper(n_amount - coins[j]) + 1,DP[n_amount]) 
            return DP[n_amount] 
        
        n = coin_helper(amount)
        return n if n != float('inf') else -1

"""
