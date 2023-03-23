from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ht = Counter(words)
        data = [(-v,k) for k,v in ht.items()]
        largest = heapq.nsmallest(k,data)
        return [x[1] for x in largest]
