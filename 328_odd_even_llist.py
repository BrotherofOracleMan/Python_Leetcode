# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currentevenhead = ListNode(0)
        evenhead = currentevenhead 
        currentoddhead = ListNode(0)
        oddhead = currentoddhead
        switch = True
        
        while(head):
            if switch:
                currentoddhead.next = ListNode(head.val)
                currentoddhead = currentoddhead.next
            else:
                currentevenhead.next = ListNode(head.val)
                currentevenhead = currentevenhead.next

            head = head.next
            switch = not switch 

        currentoddhead.next = evenhead.next
            
        return oddhead.next
