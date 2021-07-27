# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parents = {}
        
        def dfs(child,parent):
            parents[child] = parent
            if child.left:
                dfs(child.left,child)
            if child.right:
                dfs(child.right,child)
        
        dfs(root,None)
        
        dq = deque()
        dq.append([target,0])
        seen = {target}
        
        while dq:
            node , dist  = dq.popleft()
            if dist == k:
                return [node.val] + [node.val for node, d in dq]
            for node in (node.left,node.right,parents[node]):
                if node and node not in seen:
                    seen.add(node)
                    dq.append([node,dist+1])
        return []
