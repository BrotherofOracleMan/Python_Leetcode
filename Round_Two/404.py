# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        n_sum = 0
        dfs_stack = [root]
        while len(dfs_stack):
            item = dfs_stack.pop()
            if item.left:
                if item.left.right == None and item.left.left == None:
                    n_sum += item.left.val
                dfs_stack.append(item.left)
            if item.right:
                dfs_stack.append(item.right)
        return n_sum
