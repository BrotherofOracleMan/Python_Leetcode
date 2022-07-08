class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carryover = 0
        iter_num = len(digits) -1
        digits[-1] = digits[-1] + 1
        
                      
        while iter_num >= 0:
            value =(digits[iter_num] + carryover)%10
            carryover = (digits[iter_num] + carryover)//10
            digits[iter_num] = value
            iter_num -=1
        
        return [1] + digits if carryover else digits 

        
        
