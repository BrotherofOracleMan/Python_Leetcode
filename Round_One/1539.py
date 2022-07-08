class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k < arr[0]:  #if the first digit is greater than all the other first digits, just return k
            return k 
        k -= (arr[0] - 1) # get rid of all the digits before the first
        for i in range(0,len(arr)-1):
            current = (arr[i+1]- arr[i] -1) #get rid of digits between two digits 
            if current >= k: #if current gap is greater than the number of digits
                return arr[i] + k #  get number
            k -= current # reduce number of digits

        return arr[-1] + k # return k th digit after 
        
