# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse_linked_list(self, head , num):
        current_node = head
        previous_node = None
        next_node = None

        while current_node != None and num > 0:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            num-=1
        return previous_node , next_node

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length  = 0
        node_counter = head

        while node_counter != None:
            length +=1
            node_counter = node_counter.next
        
        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val

        middle = length//2
        node_after_middle_node, middle_node = self.reverse_linked_list(head, middle)
        
        if length%2 == 1:
            middle_node = middle_node.next

        while node_after_middle_node!= None and  middle_node != None:
            if node_after_middle_node.val != middle_node.val:
                return False
            node_after_middle_node = node_after_middle_node.next
            middle_node = middle_node.next
        return True
