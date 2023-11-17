import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sol, heap = [] , []

        for index, value in enumerate(mat):
            heap.append((value.count(1),index))

        heapq.heapify(heap)

        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
            
        return sol
