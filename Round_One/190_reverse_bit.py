class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        _sum , power  = 0, 31
        
        while n > 0:
            _sum += (n&1) << power
            n = n >> 1
            power -= 1
        return _sum
