# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right   
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_helper(root):
            if root is None:
                return [0,0]

            left = rob_helper(root.left)
            right = rob_helper(root.right)

            rob = root.val + left[1] + right[1]
            
            not_rob = max(left) + max(right)
            
            return [rob, not_rob]
        
        return max(rob_helper(root))
