# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        n = 1
        oldtail = head
        # get size and last node
        while oldtail.next != None:
            oldtail = oldtail.next
            n+=1
        oldtail.next = head
        #reattach to head
        newtail = head
        # return head and tail and disconnectt
        for _ in range(n - k%n -1):
            newtail = newtail.next
        newhead = newtail.next
        newtail.next = None
        
        return newhead
