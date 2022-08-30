# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        q.append([root,0])
        columnTable = defaultdict(list)
        get_min, get_max = 0 , 0
        while q:
            node,col = q.popleft()
            if node:
                columnTable[col].append(node.val)
                get_min = min(get_min, col)
                get_max = max(get_max, col)
                q.append([node.left, col - 1])
                q.append([node.right, col + 1])
        return [columnTable[x] for x in range(get_min, get_max+1)]
