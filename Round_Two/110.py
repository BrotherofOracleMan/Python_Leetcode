# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def height_helper(self,root):
        if root == None:
            return 0
        left = self.height_helper(root.left)
        right = self.height_helper(root.right)
        return max(left,right) + 1
    
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True     
        if abs(self.height_helper(root.left) - self.height_helper(root.right)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left) 
