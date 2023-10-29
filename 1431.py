class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        current_max = max(candies)
        ans = []
        for i in range(n):
            if candies[i] + extraCandies >= current_max:
                ans.append(True)
            else:
                ans.append(False)
        return ans
