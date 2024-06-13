class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def get_max(r, c):
            max_val = float("-inf")
            for i in range(r,r + 3):
                for j in range(c, c+ 3):
                    max_val = max(max_val, grid[i][j])
            return max_val

        n = len(grid)
        matrix = [[0 for i in range(n-2)] for j in range(n-2)]

        
        for r_pos in range(n-2):
            for c_pos in range(n-2):
                matrix[r_pos][c_pos] = get_max(r_pos, c_pos)
        
        return matrix
