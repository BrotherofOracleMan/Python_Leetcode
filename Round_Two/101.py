# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(left, right):
            if left == None and right == None:
                return True
            if (left == None or right==None) or left.val != right.val:
                return False
            return isSymmetric(left.left,right.right) and isSymmetric(left.right, right.left)
        return isSymmetric(root, root)
