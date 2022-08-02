class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        used_rooms = 0
        start_ptr = 0
        end_ptr = 0
        n = len(intervals)
        start_times = sorted(x[0] for x in intervals)
        end_times = sorted(x[1] for x in intervals)
        while start_ptr < n:
            if start_times[start_ptr] >= end_times[end_ptr]:
                used_rooms -=1
                end_ptr +=1
            used_rooms +=1
            start_ptr +=1
            
        return used_rooms 
