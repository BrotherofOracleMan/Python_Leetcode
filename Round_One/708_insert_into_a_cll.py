"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            NewNode = Node(insertVal,None)
            NewNode.next = NewNode
            return NewNode
        
        toInsert = False
        prev,curr=head,head.next
        while True:
            #normal case
            if prev.val <= insertVal <= curr.val:
                toInsert = True
            #tail case
            elif prev.val > curr.val:
                if insertVal > prev.val or insertVal < curr.val:
                    toInsert = True
            if toInsert:
                prev.next = Node(insertVal,curr)
                return head
            prev,curr = curr, curr.next  
            
            #single node case
            if head == prev:
                break
        prev.next = Node(insertVal,curr)
        return head
