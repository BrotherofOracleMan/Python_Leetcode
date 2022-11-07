class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        newstart,newend = newInterval
        idx,n = 0, len(intervals)
        ans = []

        while idx < n and intervals[idx][0] < newstart:
            ans.append(intervals[idx])
            idx += 1
        if not ans or ans[-1][1] < newstart:
            ans.append([newstart,newend])
        else:
            if ans[-1][1] < newend:
                ans[-1][1] =max(ans[-1][1],newend)
        while idx < n:
            current_interval = intervals[idx]
            idx +=1
            if ans[-1][1] < current_interval[0]:
                ans.append(current_interval)
            else:
                if ans[-1][1] < current_interval[1]:
                    ans[-1][1] =max(ans[-1][1],current_interval[1])
        return ans
