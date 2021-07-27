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
        dq = deque()
        val_dict = defaultdict(int)
        return_list = []
        dq.append([root,0])
        
        if root is None:
            return None
        
        while len(dq) > 0:
            size = len(dq)
            for element in range(size):
                node,val = dq.popleft()
                val_dict[node.val] = val
                if node.left:
                    dq.append([node.left,val+1])
                if node.right:
                    dq.append([node.right,val+1])
        
        target_height = val_dict[target.val]
        
        for key, value in val_dict.items():
            if key == target.val:
                continue
            if abs(value - target_height) == k:
                return_list.append(key)
            elif value + target_height == k:
                return_list.append(key)
        return return_list
            
