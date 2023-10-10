class Solution:
    def arrangeCoins(self, n: int) -> int:
        left , right = 0,n
        mid, measure = 0, 0

        while left <= right:
            mid = left + (right -left)//2
            measure = (mid*(mid +1))//2

            if measure == n:
                return int(mid)
            
            if measure > n:
                right = mid -1
            else:
                left = mid + 1
        return int(right)
