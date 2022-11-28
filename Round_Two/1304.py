class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        ans = []
        if n%2:
            ans.append(0)
        for i in range(1, n, 2):
            ans.append(-1 * i)
            ans.append(i)
        return ans
        """
        return range(1-n,n,2)
