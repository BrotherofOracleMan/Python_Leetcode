# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getsize(root):
            if root is None:
                return 0
            return 1 + getsize(root.left) + getsize(root.right)
        
        def isBST(low,high,root):
            if root is None:
                return True
            if(high != None and root.val >= high.val) or (low != None and root.val <= low.val):
                return False
            return isBST(low,root,root.left) and isBST(root,high,root.right)
        
        if not root:
            return 0 
        dq= deque()
        dq.append(root)
        max_val  = 0
        while len(dq) > 0:
            curr_size = len(dq)
            for i in range(0,curr_size):
                node = dq.popleft()
                if(isBST(None,None,node)):
                    max_val = max(max_val,getsize(node))
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return max_val
        
