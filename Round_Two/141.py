# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow_ptr = head
        fast_ptr = head.next
        while slow_ptr != fast_ptr:
            if not fast_ptr or not fast_ptr.next:
                return False
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return True
