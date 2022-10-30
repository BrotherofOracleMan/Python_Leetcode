class MyQueue:

    def __init__(self):
        self.aux_stack = []
        self.current_stack = [] 
        self.front = 0

    def push(self, x: int) -> None:
        if not self.current_stack:
            self.front = x
        self.current_stack.append(x)

    def pop(self) -> int:
        if not len(self.aux_stack):
            while len(self.current_stack):
                self.aux_stack.append(self.current_stack.pop())
        return self.aux_stack.pop()


    def peek(self) -> int:
        if not self.empty():
            if len(self.aux_stack):
                return self.aux_stack[-1]
            return self.front

    def empty(self) -> bool:
        return True if not len(self.aux_stack) and not len(self.current_stack) else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
