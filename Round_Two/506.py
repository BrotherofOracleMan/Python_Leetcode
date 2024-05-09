import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = []
        heap = []
        number_map = dict()
        index = 0

        for s in score:
            heapq.heappush(heap, -1 * s)

        while heap:
            index += 1
            max_val = heapq.heappop(heap) * -1
            number_map[max_val] = str(index)
            if index == 1:
                number_map[max_val] = "Gold Medal"
            if index == 2:
                number_map[max_val] = "Silver Medal"
            if index == 3:
                number_map[max_val] = "Bronze Medal"
                
