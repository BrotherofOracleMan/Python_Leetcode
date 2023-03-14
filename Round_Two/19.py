# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        prev = None
        length = 0

        while temp != None and temp.next != None:
            length += 1
            temp = temp.next
        
        temp = head
        
        if length -  n + 1 == 0:
            head = head.next
            return head

        for i in range(length - n + 1):
            prev = temp
            temp = temp.next
            
        next_node = temp.next
        temp.next = None
        prev.next = next_node
        return head
