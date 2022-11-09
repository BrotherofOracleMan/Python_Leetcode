# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        ans = []
        levels = 0
        dq.append(root)
        if not root:
            return ans
            
        while dq:
            ans.append([])
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                ans[levels].append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            levels +=1
        return ans
