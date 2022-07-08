# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def checksubtree(r1,r2):
            if r1 == None and r2 == None:
                return True
            elif r1==None or r2 == None:
                return False
            
            return r1.val == r2.val and checksubtree(r1.left,r2.left) and checksubtree(r1.right,r2.right)
            
        if root is None:
            return False
        if root.val == subRoot.val and checksubtree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
