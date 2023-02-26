class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_x = len(board)
        max_y = len(board[0])
        x_add = [1,0,-1,0]
        y_add = [0,1,0,-1]

        def check_boundaries(curr_x, curr_y):
            if curr_x < 0:
                return False
            if max_x <= curr_x:
                return False
            if curr_y < 0:
                return False
            if max_y <= curr_y:
                return False
            return True

        def word_search_backtracking(x,y,suffix):
            if len(suffix) == 0:
                return True
            if not check_boundaries(x,y) or board[x][y] != suffix[0]:
                return False
            board[x][y] = "#"
            for l in range(4):
                new_x = x + x_add[l]
                new_y = y + y_add[l]
                if word_search_backtracking(new_x,new_y,suffix[1:]):
                    return True
            board[x][y] = suffix[0]
            return False

        for i in range(max_x):
            for j in range(max_y):
                if board[i][j] == word[0]:
                    if word_search_backtracking(i,j,word):
                        return True
        return False
