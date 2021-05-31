class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_stack = []
        self.aux_stack = []
        self.front = -1

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.main_stack) == 0:
            self.front = x
        self.main_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.aux_stack:
            while self.main_stack:
                self.aux_stack.append(self.main_stack.pop())
        
        return self.aux_stack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        #keep track where append is
        if not self.aux_stack:
            return self.front
        else:
            return self.aux_stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.main_stack and not self.aux_stack:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
