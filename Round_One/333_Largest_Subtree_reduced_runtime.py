# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SubTree(object):
    def __init__(self, largest, n, min, max):
            self.largest = largest  # largest BST
            self.n = n              # number of nodes in this ST
            self.min = min          # min val in this ST
            self.max = max          # max val in this ST

class Solution(object):
    def dfs(self,root):
        if root is None:
            return SubTree(0,0,float('inf'),float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        n = 0
        if root.val > left.max and root.val < right.min:
            print(n)
            n = left.n + right.n + 1
        else:
            n = float('-inf')
        largest = max(right.largest,left.largest,n)
        return SubTree(largest,n,min(left.min,root.val),max(right.max,root.val))
        
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree = self.dfs(root)
        return tree.largest
        
