"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        nsum = sum(arr)
        odd = 3
        while odd <= len(arr):
            for i in range(0,len(arr)-odd+1):
                nsum += sum(arr[i:i+odd])
            odd+=2
        return nsum
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n_sum = 0
        for i in range(0, len(arr)+1):
            for j in range(i+1,len(arr)+1):
                if(j-i)%2==1:
                    n_sum +=sum(arr[0:j])-sum(arr[0:i])
        return n_sum
                    
