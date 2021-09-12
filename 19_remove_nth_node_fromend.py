# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        current = head
        # Get size of the linkedlist
        
        while current:
            size += 1
            current = current.next
        
        print(size)
        if n == 1 and size == 1:
            return None
        elif n == size:
            head = head.next
            return head
        else:
            current = head
            for i in range(size - n -1):
                print("Test")
                current = current.next
            current.next = current.next.next
        return head
            
