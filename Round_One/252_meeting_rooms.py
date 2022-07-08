class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
  
        
        if len(intervals) <= 1:
            return True
        
        intervals.sort()
        prev_interval = intervals[0]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < prev_interval[1]:
                return False
            prev_interval = intervals[i]
        return True
        
