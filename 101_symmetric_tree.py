# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetricHelper(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            return(p.val == q.val) and isSymmetricHelper(p.left,q.right) and isSymmetricHelper(p.right,q.left)
        
        p = root
        q = root
        return isSymmetricHelper(p,q)
