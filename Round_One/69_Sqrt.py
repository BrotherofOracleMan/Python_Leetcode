class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x< 2:
            return x 
        mid = 0
        left = 0
        right = x//2
        
        while left <= right:
            mid = left + (right-left)//2
            if mid * mid == x:
                return mid
            if mid * mid < x:   
                left = mid + 1
            else:
                right = mid -1
            
        return right # you need to return the lesser one floor()
            
            
