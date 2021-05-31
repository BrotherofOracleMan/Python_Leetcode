class MaxStack(object):
    #can also use Double linked list and Tree Map Approach(Only Read about this)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.aux_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.main_stack) == 0:
            self.main_stack.append([x,x])
        else:
            self.main_stack.append([x,max(x,self.main_stack[-1][1])])
        
    def pop(self):
        """
        :rtype: int
        """
        return self.main_stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.main_stack[-1][0]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.main_stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        currentMax = self.peekMax()
        while(self.main_stack[-1][0] != currentMax):
            self.aux_stack.append(self.main_stack.pop()[0])
        self.main_stack.pop()
        
        while(len(self.aux_stack) > 0):
            self.push(self.aux_stack.pop())
        
        return currentMax
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
