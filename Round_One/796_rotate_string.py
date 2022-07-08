class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        search_string = s + s
        
        return len(s) == len(goal) and goal in search_string
