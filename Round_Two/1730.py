from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        bfs_q = deque()
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    bfs_q.append([i,j,0])
                    break
  
        while(len(bfs_q) > 0):
            x,y,step = bfs_q.popleft()
            for coord_x, coord_y in [[1,0],[0,1],[-1,0],[0,-1]]:
                new_x = x + coord_x
                new_y = y + coord_y
                if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols and grid[new_x][new_y] in ["#",'O']:
                    if grid[new_x][new_y] == "#":
                        return step + 1
                    grid[new_x][new_y] = "|"
                    bfs_q.append([new_x, new_y, step+1]) 
        return -1
