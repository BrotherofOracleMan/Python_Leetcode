class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left,right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)

        while left < right:      
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
            curr_max_height = min(height[left], height[right])
            max_area = max(max_area,(right - left) * curr_max_height)
        return max_area
