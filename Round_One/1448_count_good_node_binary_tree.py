# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        
        def goodNodesHelper(root, currMax):
            if root is None:
                return 0
            if root.val >= currMax:
                return 1+ goodNodesHelper(root.left,root.val) + goodNodesHelper(root.right, root.val)
            else:
                return goodNodesHelper(root.left,currMax) + goodNodesHelper(root.right,currMax)
        
        return goodNodesHelper(root,float('-inf'))
