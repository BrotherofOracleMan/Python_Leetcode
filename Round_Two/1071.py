import math

class Solution:
    def valid(self, str1, str2, k):
        len1 , len2  = len(str1) //k , len(str2)//k
        str_base = str1[:k]
        return len1 * str_base == str1 and len2 * str_base == str2

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0 , -1):
            if self.valid(str1, str2,i ):
                return str1[:i]
        return ""
