class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, sr, sc, color, newcolor, rows, cols):
            if image[sr][sc] == color:
                image[sr][sc] = newcolor
                if sr >=1:dfs(image,sr-1, sc, color, newcolor,rows, cols)
                if sc >=1:dfs(image,sr, sc-1, color, newcolor,rows, cols)
                if sr + 1< rows: dfs(image,sr+1, sc, color, newcolor,rows, cols)
                if sc + 1 < cols: dfs(image,sr, sc+1, color, newcolor,rows, cols)
        new_color = color
        color = image[sr][sc]
        if image[sr][sc] == new_color: return image
        rows, cols  = len(image) , len(image[0]) 
        dfs(image,sr,sc,color,new_color,rows, cols)
        return image
