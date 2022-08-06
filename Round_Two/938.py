# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        bfs = deque()
        bfs.append(root)
        node_sum = 0
        
        while bfs:
            size = len(bfs)
            while size > 0:
                node_val = bfs.popleft()
                if node_val != None and node_val.val >= low and node_val.val <= high:
                    node_sum += node_val.val
                if node_val.left:
                    bfs.append(node_val.left)
                if node_val.right:
                    bfs.append(node_val.right)
                size -=1
        return node_sum
