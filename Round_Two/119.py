class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for row in range(rowIndex + 1):
            curr_row =[None for i in range(row+1)]
            curr_row[0], curr_row[-1] = 1, 1
            for i in range(1, len(curr_row) -1):
                curr_row[i] = triangle[row -1][i] + triangle[row-1][i-1]
            triangle.append(curr_row)
        return triangle[rowIndex]
        
