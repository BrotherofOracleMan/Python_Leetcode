# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.n  ext = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        N = 0
        get_size_head  =  head
        while get_size_head != None:
            N +=1
            get_size_head = get_size_head.next
        
        partsize ,addOne = divmod(N,k)
        parts = 0
        partsizes = [partsize + 1 if i<addOne else partsize for i in range(k) ]
        
        sol = []
        
        
        while parts < k:
            if head is None:
                sol.append(None)
            else:
                sol.append(head)
                for _ in range(partsizes[parts] -1):
                    head = head.next
                temp = head.next
                head.next = None
                head = temp
                
            parts+=1
            
        return sol
        
        
