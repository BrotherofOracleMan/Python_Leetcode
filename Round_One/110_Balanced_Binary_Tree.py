# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def __init__():
            self.isBalanced = True
        
        def maxDepth(root):
            if root is None:
                return 0
            return max(maxDepth(root.left),maxDepth(root.right)) + 1
        
        def isBalancedHelper(root):
            if root is None:
                return True
            if abs(maxDepth(root.left) - maxDepth(root.right)) > 1:
                return False
            return isBalancedHelper(root.left) and isBalancedHelper(root.right)
        
        return isBalancedHelper(root)
