class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1

        for i in range(0, 32):
            if n & mask:
                bits += 1
            mask = mask << 1
        return bits


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while(n != 0):
            n = n &(n-1)
            bits +=1
        return bits
