# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
        self.peek = None
        self.generator = self.create_generator(nestedList)
    
    def create_generator(self,nestedList):
        for val in nestedList:
            if val.isInteger():
                yield val.getInteger()
            else:
                yield from self.create_generator(val.getList())
        
    def next(self) -> int:
        if not self.hasNext(): 
            return None
        next_num , self.peek = self.peek, None
        return next_num
        

    def hasNext(self) -> bool:
        if self.peek is not None:
            return True
        try:
            self.peek = next(self.generator)
            return True
        except:
            return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
