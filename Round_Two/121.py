class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        min_buy = float('inf')
        
        for i in range(0, len(prices)):
            if prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy
            min_buy = min(min_buy,prices[i])
        return max_profit if max_profit > 0 else 0
        
        
        
