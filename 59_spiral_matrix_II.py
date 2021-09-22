class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        start,final_num = 1 , n * n
        top , bot = 0 ,n -1
        left , right  = 0 , n -1
        final_table = [n * [0] for _ in range(n)]
        
        if n==1:
            return [[1]]
        
        while bot >= top and right >= left: 
            for i in range(left,right+1):
                final_table[top][i] = start
                start +=1
            top+=1
            
            for i in range(top,bot+1):
                final_table[i][right] = start
                start +=1
            right-=1
            
            for i in range(right,left-1,-1):
                final_table[bot][i] = start
                start+=1
            bot-=1            
            
            
            for i in range(bot,top-1,-1):
                final_table[i][left] = start
                start+=1
            left+=1
            
        return final_table
        
