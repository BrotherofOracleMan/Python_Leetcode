
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = -1
        q = deque()
        four_directions = [[0,1],[1,0],[0,-1],[-1,0]]
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh_oranges +=1
                    
        while len(q) > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for x, y in four_directions:
                    new_x = row + x
                    new_y = col + y
                    if new_x >= 0 and new_y >= 0 and new_x < len(grid) and new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.append([new_x,new_y])
            time += 1
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return time if fresh_oranges != 0 else 0               
