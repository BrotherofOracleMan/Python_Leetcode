class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(visited_set,grid,r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            if visited_set[r][c] == False:
                visited_set[r][c] = True
                dfs(visited_set,grid,r+1,c)
                dfs(visited_set,grid,r,c-1)
                dfs(visited_set,grid,r,c+1)
                dfs(visited_set,grid,r-1,c)
        
        visited_set = [ [False for elem in grid[0]] for elem in grid]
        numberOfIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and visited_set[row][col] == False:
                    dfs(visited_set,grid,row,col)
                    numberOfIslands += 1
        print(visited_set)
        return numberOfIslands
        
