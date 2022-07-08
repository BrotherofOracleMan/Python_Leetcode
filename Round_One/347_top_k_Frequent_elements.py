
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        
        Freq_table = dict()
        mfe = []
        
        for element in nums:
            if element not in Freq_table:
                Freq_table[element] = 1
            else:
                Freq_table[element] += 1
     
        return heapq.nlargest(k,Freq_table.items(),key=Freq_table.get)
                
        
        
