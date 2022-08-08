# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter= 0
        def diameter_helper(root):            
            nonlocal diameter
            if root == None:
                return 0
            left = diameter_helper(root.left)
            right = diameter_helper(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left,right)
        hieght = diameter_helper(root)
        return diameter
        
