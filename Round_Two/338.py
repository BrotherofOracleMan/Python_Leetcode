class Solution:
    def countBits(self, n: int) -> List[int]:
        array = (n+1) * [0]
        """
        for i in range(0, n+1):
            array[i] = self.getBits(i)
        """
        for i in range(1, n+1):
            array[i] = array[i & (i-1)] + 1
        return array

    def getBits(self,n):
        bits = 0
        while n != 0:
            n = n &(n-1)
            bits+=1
        return bits
