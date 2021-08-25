class Solution(object):
    
    def __init__(self):
        self.max_val = 0
    
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def backtrack(index,array,string):
            if len(string) == len(set(string)):
                self.max_val = max(self.max_val,len(string))
            else:
                return 
            
            for i in range(index, len(array)):
                backtrack(i+1,array,string + array[i])
            
            return
                        
        backtrack(0,arr,"")
        return self.max_val