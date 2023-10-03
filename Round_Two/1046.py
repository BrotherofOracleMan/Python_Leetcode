import heapq

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def push(self, stone_weight):
        heapq.heappush(self.heap, -1 * stone_weight)

    def pop(self):
        return -1 * heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_pq = MaxHeap()
        if len(stones) == 1:
            return stones[-1]
            
        for stone in stones:
            max_pq.push(stone)
        
        while max_pq.size() > 1:
            y, x = max_pq.pop() , max_pq.pop()
            if y> x:
                max_pq.push(y-x)
        return max_pq.pop() if max_pq.size() else 0
