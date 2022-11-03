class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort()
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < current_interval[1]:
                return False
            current_interval = intervals[i]
        return True
