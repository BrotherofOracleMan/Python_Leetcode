class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        prev  = None
        stack = [head]
        
        while len(stack) > 0:
            current = stack.pop()
            
            if current and current.next:
                stack.append(current.next)
            if current and current.child:
                stack.append(current.child)
                current.child = None
            if current:
                if prev:
                    prev.next = current
                    current.prev = prev
            prev = current
    
        return head
