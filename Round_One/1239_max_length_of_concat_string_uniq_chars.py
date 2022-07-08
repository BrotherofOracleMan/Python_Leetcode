class Solution(object):
    
    def __init__(self):
        self.max_val = 0
    
    def checkifunique(self, arr):
        hash_table = dict()
        for word in arr:
            for char in word:
                if char in hash_table.keys():
                    return False
                else:
                    hash_table[char] = 1
        return True
    
    def getlength(self,arr):
        length = 0
        for word in arr:
            for char in word:
                length +=1
        return length
    
    
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def backtrack(index,word_list,array,length):
            if self.checkifunique(word_list) == False:
                return
            if self.checkifunique(word_list):

                self.max_val = max(self.max_val,self.getlength(word_list))
                
            for i in range(index ,len(array)):
                word_list.append(array[i])
                backtrack(i+1,word_list,array,length)
                word_list.pop()
                        
        backtrack(0,[],arr,len(arr))
        return self.max_val