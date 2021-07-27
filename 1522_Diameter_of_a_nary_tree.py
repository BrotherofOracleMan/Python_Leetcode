"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diameter = 0
        
        def height(root):
            if len(root.children) == 0:
                return 0
            max_height1,max_height2 = 0,0
            
            for node in root.children:
                parent_height = height(node)+1
                if parent_height > max_height1:
                    max_height1,max_height2 = parent_height, max_height1
                elif parent_height > max_height2:
                    max_height2 = parent_height
                
            self.diameter = max(max_height1 + max_height2, self.diameter)
            
            return max_height1
        
        height(root)
        return self.diameter 
