# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_set = set()
        while headA != None:
            node_set.add(headA)
            headA = headA.next
        
        while headB != None:
            if headB in node_set:
                return headB
            headB = headB.next
        return None
        
