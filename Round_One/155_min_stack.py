class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else:
            min_value = min(val,self.stack[-1][1])
            self.stack.append([val,min_value])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        
        return None
    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
