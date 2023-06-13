class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        solution = [[0]*m for i in range(n)]
        solution[0][0] = grid[0][0]

        for i in range(1,m):
            solution[0][i] = solution[0][i-1] + grid[0][i]

        for i in range(1,n):
            solution[i][0] = solution[i-1][0] + grid[i][0]

        for row in range(1,n):
            for col in range(1,m):
                solution[row][col] = grid[row][col] + min(solution[row-1][col], solution[row][col-1])
        return solution[n-1][m-1]
