# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        head = ListNode(0)
        current = head

        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                current.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                current.next = ListNode(ptr2.val)
                ptr2=ptr2.next
            current = current.next
        current.next = ptr1 or ptr2
        return head.next
