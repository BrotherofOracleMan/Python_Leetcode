class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        ans = ""
        ptr_1 = len(a) -1
        ptr_2 = len(b) -1
        num1 = 0
        num2 = 0
        while ptr_1 >= 0 or ptr_2 >= 0:
            if ptr_1 >= 0:
                num1 = int(a[ptr_1])
            else: 
                num1 = 0
            if ptr_2 >= 0:
                num2 = int(b[ptr_2])
            else:
                num2 = 0
            number = carry_over + num1 + num2
            carry_over = number // 2
            number = number %2
            ans = ("1" if number else "0") + ans
            ptr_1 -=1
            ptr_2 -= 1

        if carry_over == 1:
            ans = "1" + ans
        return ans
