class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        max_sum = 0
        t_sum = 0
        i = 0
        n = len(customers)
        for j in range(len(grumpy)):
            t_sum += customers[j] * (1 if grumpy[j] == 0 else 0) 
        
        for j in range(len(grumpy)):
            if grumpy[j]:
                t_sum += customers[j]
            if (j -i + 1) == minutes:
                max_sum = max(t_sum, max_sum)
                if grumpy[i]:
                    t_sum -= customers[i]
                i+=1
        return max_sum
