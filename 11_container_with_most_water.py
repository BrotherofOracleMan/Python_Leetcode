class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left , right = 0 , len(height) - 1
        max_area = float("-inf")
        
        while left < right:
            max_area = max((right-left)* min(height[left],height[right]), max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left +=1
        
        return max_area
