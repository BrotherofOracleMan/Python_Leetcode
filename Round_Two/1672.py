class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = float('-inf')
        for i in range(len(accounts)):
            temp_sum = sum(accounts[i])
            max_num = max(max_num, temp_sum)
        return max_num
