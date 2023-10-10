class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp_x = x
        reversed_num , remainder , original = 0, 0 , x

        while temp_x!= 0:
            remainder = temp_x % 10
            reversed_num = reversed_num * 10 + remainder
            temp_x = int(temp_x/10)
        print(reversed_num)
        return reversed_num == original
        
