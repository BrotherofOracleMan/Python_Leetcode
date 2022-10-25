class Solution:
    def isPalindrome(self, s: str) -> bool:
        left , right  = 0, len(s) -1

        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right-=1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1
        return True

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome_str = ""

        for char in s:
            if char.isalnum():
                palindrome_str += char.lower()
        for i in range(0,len(palindrome_str)//2):
            if palindrome_str[i] != palindrome_str[len(palindrome_str) -1 - i]:
                return False
        return True

"""
