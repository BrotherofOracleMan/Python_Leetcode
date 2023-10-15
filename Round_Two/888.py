class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB, delta = 0,0,0
        for a in aliceSizes:
            sumA += a
        for b in bobSizes:
            sumB += b
        delta = (sumB - sumA)//2

        setB = set()

        for b in bobSizes:
            setB.add(b)
        
        for a in aliceSizes:
            if a + delta in setB:
                return [a, a + delta] 
        return [0,0]
