class MovingAverage:

    def __init__(self, size: int):
        self.queue_size = 0
        self.max_size = size
        self.q = deque()
        self.sum = 0.0

    def next(self, val: int) -> float:
        self.queue_size +=1
        self.q.append(val)
        tailval = self.q.popleft() if self.queue_size > self.max_size else 0
        self.sum = self.sum - tailval + val
        return self.sum/min(self.queue_size,self.max_size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


"""
class MovingAverage:

    def __init__(self, size: int):
        self.queue_size = 0
        self.max_size = size
        self.q = deque()
        self.sum = 0.0

    def next(self, val: int) -> float:
        self.queue_size +=1
        self.q.append(val)
        tailval = self.q.popleft() if self.queue_size > self.max_size else 0
        self.sum = self.sum - tailval + val
        return self.sum/min(self.queue_size,self.max_size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
"""
