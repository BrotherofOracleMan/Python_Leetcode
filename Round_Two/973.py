import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        ans = []
        for point in points:
            heapq.heappush(hq,((math.sqrt(point[0]**2 + point[1] **2), point)))

        for i in range(0 ,k):
            ans.append(heapq.heappop(hq)[1])
        return ans
