class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = k * [-1]
        self.size = 0 
        self.capacity = k 
        self.headindex = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.queue[(self.size + self.headindex)% self.capacity] = value
            self.size +=1
            return True
           

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.headindex] = -1         
            self.headindex = ((self.headindex + 1) %self.capacity)
            self.size -=1 
            return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.headindex]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.headindex+self.size -1)%self.capacity]
            

    def isEmpty(self):
        """
        :rtype: bool
        """
        return True if self.size == 0 else False

    def isFull(self):
        """
        :rtype: bool
        """
        return True if self.size == self.capacity else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
