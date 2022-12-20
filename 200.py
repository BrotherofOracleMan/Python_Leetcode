class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, rows, cols, visited_lands):
            if grid[row][col] == "0" or visited_lands[row][col] == True :
                return

            visited_lands[row][col] = True
            if row >= 1 : dfs(row - 1, col, rows, cols, visited_lands)
            if col >=1 : dfs(row, col -1, rows, cols, visited_lands)
            if row + 1< rows: dfs(row+1, col, rows, cols, visited_lands)
            if col + 1< cols: dfs(row, col + 1, rows, cols, visited_lands)

        rows = len(grid)
        cols = len(grid[0])
        number_of_islands = 0

        visited_lands = [ [False for elem in grid[0]] for elem in grid]
        for row in range(0, rows):
            for col in range(0, cols):
                if not visited_lands[row][col] and grid[row][col] == "1":
                    dfs(row, col, rows, cols, visited_lands)
                    number_of_islands +=1
        return number_of_islands
