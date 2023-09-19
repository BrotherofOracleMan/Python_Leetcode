# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp_head = ListNode(-1)
        temp_head.next = head
        prev = temp_head

        current = head

        while current != None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return temp_head.next
        
