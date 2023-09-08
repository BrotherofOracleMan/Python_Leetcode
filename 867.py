class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        transposed_matrix = [[0] * n for i in range(m)]

        for r in range(n):
            for c in range(m):
                transposed_matrix[c][r] = matrix[r][c]
        return transposed_matrix
