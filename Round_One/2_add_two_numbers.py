# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        carryover = 0
        
        while l1 != None or l2 != None:
            x1 = l1.val if l1 != None else 0
            x2 = l2.val if l2 != None else 0
            value = (x1 + x2 + carryover) %10
            carryover = (x1+x2+carryover) // 10
            current.next = ListNode(value)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
       
        if carryover:
            current.next = ListNode(carryover)
        
        return head.next
