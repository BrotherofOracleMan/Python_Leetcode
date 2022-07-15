class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) == k:
            return sum(cardPoints)
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        sliding_window = 0
        min_subarray_score = total_sum
        i = 0
        for j in range(len(cardPoints)):
            sliding_window += cardPoints[j]
            if (j - i +1) == (n-k):
                min_subarray_score = min(min_subarray_score,sliding_window)
                sliding_window -= cardPoints[i]
                i+=1
        return total_sum - min_subarray_score 

