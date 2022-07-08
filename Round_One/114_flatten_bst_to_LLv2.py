# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while len(stack) > 0:
            node = stack.pop()
            if node and node.right:
                stack.append(node.right)
            if node and node.left:
                stack.append(node.left)
            if node:
                if prev:
                    prev.right = node
                    prev.left = None
                prev = node
        
