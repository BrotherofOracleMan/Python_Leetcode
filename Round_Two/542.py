class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        dq = collections.deque()
        cols = len(mat[0])
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dq.append([i,j])
                    dist[i][j] = 0
        x_add = [1,0,0,-1]
        y_add = [0,1,-1,0]

        while len(dq):
            x,y = dq.popleft()
            for i in range(4):
                new_x = x + x_add[i]
                new_y = y + y_add[i]
                if new_x >= 0 and new_y >=0 and new_x < rows and new_y < cols:
                    if dist[new_x][new_y] > dist[x][y] + 1:
                        dist[new_x][new_y] = dist[x][y] + 1
                        dq.append([new_x,new_y])
        return dist
