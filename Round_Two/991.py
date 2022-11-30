class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        before_adding_ones = 0

        while target > startValue:
            before_adding_ones +=1
            if target %2== 1:
                target +=1
            else:
                target /=2
        return before_adding_ones + startValue - target
