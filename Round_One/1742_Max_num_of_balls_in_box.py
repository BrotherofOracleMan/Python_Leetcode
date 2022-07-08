class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        
        hash_table = dict()
        
        max_val = 0
        max_index = 0
        
        for i in range(lowLimit,highLimit+1):
            _sum = 0
            n = i
            while n:
                _sum += (n%10)
                n = n/10
            if _sum not in hash_table:
                hash_table[_sum] = 1
            else:
                 hash_table[_sum] += 1
        
        for key,value in hash_table.items():
            if max_val < value:
                max_val = value
        return max_val
        
