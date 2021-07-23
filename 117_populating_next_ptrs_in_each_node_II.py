"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        dq = deque()
        dq.append(root)
        
        if root is None:
            return root
        
        while len(dq) != 0:
            last_node = None
            current_size = len(dq)
            for i in range(0,current_size):
                last_node = dq.popleft()
                
                if last_node.left:
                    dq.append(last_node.left) 
                if last_node.right:
                    dq.append(last_node.right)
                if len(dq) > 0:
                    last_node.next = dq[0]
            last_node.next = None
        
        return root
        
