# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(root)
        list_of_lists = []
        
        if root is None:
            return list_of_lists
        
        while len(queue) > 0:
            size = len(queue)
            line = []
            for i in range(size):
                element = queue.popleft()
                line.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            list_of_lists.append(line)
        return list_of_lists
            
            
