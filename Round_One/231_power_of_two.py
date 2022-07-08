class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (n-1) == 0
        
        
        """
        Unoptimized
        if n==0:
            return False
        
        while n%2 ==0:
            n /= 2
        return n == 1
        """
