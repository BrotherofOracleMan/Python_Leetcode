# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append([root,0])
        leaf_nodes =[]
        while len(q) > 0:
            len_q = len(q)
            for _ in range(len_q):
                node , height = q.popleft()
                if node and not node.left and not node.right:
                    return 1 + height
                if node and node.left:
                    q.append([node.left, height+1])
                if node and node.right:
                    q.append([node.right, height+1])
        return -1
        
