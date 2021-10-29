class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        max_units = 0
        it_ptr = 0
        boxTypes.sort(reverse=True,key = lambda a:a[1])        
        
        for boxType in boxTypes:
            boxCount = min(truckSize,boxType[0])
            max_units += boxCount * boxType[1]
            truckSize -= boxCount
            if truckSize == 0:
                break
        return max_units
