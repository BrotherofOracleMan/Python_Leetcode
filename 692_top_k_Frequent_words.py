import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        def sortkey(a):
            return -a[1], a[0]
        
        
        Freq_table = defaultdict(int) 
        
        
        for word in words:
            Freq_table[word] +=1
        list_items = heapq.nsmallest(k,Freq_table.items(),key = sortkey)
        
        return [x[0] for x in list_items ]
