"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.hashtable = {}
    
    def create_new_node(self,old_node):
        if old_node:
            if old_node in self.hashtable:
                return self.hashtable[old_node]
            else:
                self.hashtable[old_node] = Node(old_node.val)
                return self.hashtable[old_node]
                
    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        old_node = head
        
        new_node = self.create_new_node(old_node)
        
        while old_node:
            new_node.next = self.create_new_node(old_node.next)
            new_node.random = self.create_new_node(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return self.hashtable[head]
        
