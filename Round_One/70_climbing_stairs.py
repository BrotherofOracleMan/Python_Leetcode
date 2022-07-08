class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climbStairshelper(n,subproblist):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if subproblist[n] == -1:
                subproblist[n] = climbStairshelper(n-1,subproblist) + climbStairshelper(n-2,subproblist)
            return subproblist[n]
        subproblist = [-1] *(n+1)
        return climbStairshelper(n,subproblist)
