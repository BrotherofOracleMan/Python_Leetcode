class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sub_box = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                #check rows
                if int(board[i][j]) in rows[i]:
                    return False
                else:
                    rows[i].add(int(board[i][j]))
                
                #check cols
                if int(board[i][j]) in cols[j]:
                    return False
                else:
                    cols[j].add(int(board[i][j]))
                
                #check sub_box
                sub_box_indice = (i//3)*3 + j//3
                if int(board[i][j]) in sub_box[sub_box_indice]:
                    return False
                else:
                    sub_box[sub_box_indice].add(int(board[i][j]))

        return True
