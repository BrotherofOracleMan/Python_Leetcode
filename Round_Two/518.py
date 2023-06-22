class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        DP = [0] * (amount +1)
        DP[0] = 1

        for coin in coins:
            for value in range(coin, amount + 1):
                DP[value] += DP[value - coin]
        print(DP)
        return DP[-1]
