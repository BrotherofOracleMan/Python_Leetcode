class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current_intervals=[]
        current_interval= intervals[0]
        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                if intervals[i][1] > current_interval[1]:
                    current_interval[1] = intervals[i][1]
            else:
                current_intervals.append(current_interval)
                current_interval=intervals[i]
        current_intervals.append(current_interval)
        return current_intervals
