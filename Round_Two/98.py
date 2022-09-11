# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST_helper(root, low, high):
            if root is None:
                return True
            if (high is not None and root.val >= high.val) or (low is not None and root.val <= low.val):
                return False
            return isValidBST_helper(root.left,low,root) and isValidBST_helper(root.right, root, high)
        return isValidBST_helper(root, None, None)
        
