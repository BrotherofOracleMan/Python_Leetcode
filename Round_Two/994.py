from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs_q = deque()
        time_elapsed = -1
        is_fresh_still_exists = False
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    bfs_q.append([i,j])
                    
        if fresh_oranges == 0:
            return 0

        while len(bfs_q) > 0:
            q_len = len(bfs_q)
            print(bfs_q)
            for i in range(q_len):
                x,y = bfs_q.popleft()
                for coord_x, coord_y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    new_x = x + coord_x
                    new_y = y + coord_y
                    if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols:
                        if grid[new_x][new_y] != 0 and grid[new_x][new_y] != 2:
                            grid[new_x][new_y] = 2
                            bfs_q.append([new_x,new_y])
            time_elapsed+=1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    is_fresh_still_exists = True
        return time_elapsed if not is_fresh_still_exists else -1
