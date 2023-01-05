from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        bfs_q = deque()
        inDegrees = {x:0 for x in range(numCourses)}
        outNodes = {x:[] for x in range(numCourses)}

        for next_course, prev_course in prerequisites:
            inDegrees[next_course] +=1
            outNodes[prev_course].append(next_course)
        
        for node in inDegrees:
            if inDegrees[node] == 0:
                bfs_q.append(node)
        print()
        while len(bfs_q):
            course = bfs_q.pop()
            ans.append(course)
            for next_course in outNodes[course]:
                inDegrees[next_course] -= 1
                if inDegrees[next_course] == 0:
                    bfs_q.append(next_course)
        return ans if len(ans) == numCourses else []
