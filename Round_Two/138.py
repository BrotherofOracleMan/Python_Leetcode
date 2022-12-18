"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clone_dict = dict()
        clone_dict[None] = None
        t_head = head
        if t_head == None:
            return None
        index = 0
        while t_head != None:
            clone_node = Node(t_head.val)
            clone_dict[t_head] = clone_node
            index +=1
            t_head = t_head.next

        #reset the pointer
        t_head = head
        new_head = clone_dict[t_head]
        ans = new_head

        while t_head != None:
            new_head.next = clone_dict[t_head.next]
            new_head.random = clone_dict[t_head.random]
            t_head = t_head.next
            new_head = new_head.next
        return ans
