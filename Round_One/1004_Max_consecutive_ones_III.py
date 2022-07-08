class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        start = 0
        longest = 0
        numberOfZeros = 0
        for index,number in enumerate(A):
            if number is 0:
                numberOfZeros+=1
            if numberOfZeros > K:
                if A[start] is 0:
                    numberOfZeros-=1
                start += 1

            longest = max(longest,index-start+1)
        return longest                
        
