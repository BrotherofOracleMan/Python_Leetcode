class Solution:
    def __init__(self) -> None:
        self.perimeter = 0
    
    def dfs(self,i,j,visited, grid):
        edges = 4
        for add_i, add_j in [[1,0],[-1,0],[0,-1],[0,1]]:
            x = i + add_i
            y = j + add_j
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                edges -= 1
                if (x,y) not in visited:
                    visited.add((x,y))
                    self.dfs(x,y,visited, grid)
        self.perimeter += edges

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    visited = set([(i,j)])
                    self.dfs(i,j, visited, grid)
                    return self.perimeter
        return 0
