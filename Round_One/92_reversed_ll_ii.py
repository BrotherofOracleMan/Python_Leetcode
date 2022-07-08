# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        curr, prev = head, None
        # get the head and the temporary tail
        while left > 1:
            prev = curr
            curr = curr.next
            left -=1
            right -=1
        tail, after_head = curr ,prev
        
        # partial reverse between 2 and 4
        while right > 0:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
            right -= 1
        #fix the connections b
        if after_head:
            after_head.next = prev
        else:
            head = prev
        
        tail.next = curr
            
        return head
