class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        test_string = s.split()
        
        begin = 0
        end = len(test_string)
        
        for i in range(0,end//2):
            temp = test_string[begin]
            test_string[begin] = test_string[end- i-1]
            test_string[end - i -1] =  temp
            begin+=1
            
        return " ".join(test_string)
     
        
