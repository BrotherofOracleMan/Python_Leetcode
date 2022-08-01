class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []
        curr_capacity =  0
        for trip in trips:
            timestamps.append([trip[1], trip[0]])
            timestamps.append([trip[2], -1 * trip[0]])
        timestamps.sort()
        
        for timestamp,p in timestamps:
            curr_capacity += p
            if curr_capacity > capacity:
                return False
        return True
