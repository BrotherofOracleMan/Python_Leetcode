class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        
        start_times = [i[0] for i in sorted(intervals)]
        end_time = sorted([i[1] for i in intervals])
        rooms,end_ptr = 0 , 0 
        for starttime in start_times: 
            # we only care about the if end time is less than starttime to increment rooms
            # it negates b/c you end one time to start time so end_ptr+=1
            if starttime < end_time[end_ptr]:
                rooms+=1
            else:
                end_ptr+=1
        return rooms
