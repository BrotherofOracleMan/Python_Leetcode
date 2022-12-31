from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for prev_course,next_course in prerequisites:
            adj_list[prev_course].append(next_course)
        
        path = [False] * numCourses
        checked_paths = [False] * numCourses

        for course in range(numCourses):
            if self.isCyclic(course,adj_list,path,checked_paths):
                return False
        return True

    def isCyclic(self,current_course,adj_list, path, checked_paths):
        if checked_paths[current_course]:
            return False
        if path[current_course]:
            return True
            
        path[current_course] = True

        ret=False
        for child in adj_list[current_course]:
            ret = self.isCyclic(child, adj_list, path, checked_paths)
            if ret: break

        path[current_course] = False

        checked_paths[current_course] = True

        return ret
