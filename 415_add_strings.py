class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        iter_num1 = len(num1) - 1
        iter_num2 = len(num2) - 1
        carry_over = 0
        final_string = ""
        while iter_num1 >= 0 or iter_num2 >= 0:
            x1 = int(num1[iter_num1]) if iter_num1 >= 0 else 0
            x2 = int(num2[iter_num2]) if iter_num2 >=0  else 0
            value = (x1+x2+carry_over)%10
            carry_over = (x1+x2+carry_over)//10
            final_string = str(value) + final_string
    
            iter_num1-=1
            iter_num2-=1
        
        if carry_over:
            final_string = "1" + final_string            
            
        return final_string
