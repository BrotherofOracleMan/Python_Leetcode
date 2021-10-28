class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        x,y,idx = 0,0,0
        for char in instructions:
            if char == "L":
                idx = (idx + 3)%4
            elif char == "R":
                idx = (idx + 1) %4
            else:
                x = x + directions[idx][0]
                y = y + directions[idx][1]
        return (x == 0 and y==0) or idx != 0
