import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [(-1 * c[x[0]],x[0]) for x in c]
        heapq.heapify(heap)

        max_freq = -1 * heapq.heappop(heap)[0]
        idle_slots = (max_freq - 1) * n
        
        n_max = 1
        while heap:
            freq = -1 * heapq.heappop(heap)[0]
            if freq == max_freq:
                n_max +=1
        return max((n+1) * (max_freq -1) + n_max,len(tasks))

"""
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [(-1 * c[x[0]],x[0]) for x in c]
        heapq.heapify(heap)

        max_freq = -1 * heapq.heappop(heap)[0]
        idle_slots = (max_freq - 1) * n
        
        while heap:
            freq = -1 * heapq.heappop(heap)[0]
            idle_slots -= min(max_freq-1, freq)

        return max(idle_slots,0) + len(tasks)

"""
