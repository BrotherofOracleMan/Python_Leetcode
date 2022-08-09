# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        MinclosestValue = float("inf")
        while root:
            MinclosestValue = min(root.val,MinclosestValue, key = lambda x: abs(target - x))
            root = root.right if target > root.val else root.left
        return MinclosestValue
            
        
