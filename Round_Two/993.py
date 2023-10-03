from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        d_q = deque()
        d_q.append(root)

        while d_q:
            siblings, cousins = False, False
            size = len(d_q)
            for _ in range(size):
                node = d_q.popleft()
                if node == None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            return not siblings
                    if node.left:
                        d_q.append(node.left)
                    if node.right:
                        d_q.append(node.right)
                    d_q.append(None)
            if cousins:
                return False
        return False
