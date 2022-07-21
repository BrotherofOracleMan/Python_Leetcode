class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        curr_height = [0]
        for i in range(n):
            curr_height.append(curr_height[i] + gain[i])
        return max(curr_height)
            
        """
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        curr_height = 0
        highest_alt = 0
        for i in range(n):
            highest_alt = max(curr_height,highest_alt)
            curr_height += gain[i]
        return max(highest_alt, curr_height)
            
        """
