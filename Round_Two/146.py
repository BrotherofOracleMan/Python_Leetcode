class LRUCache:

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.size = capacity
        self.cache = OrderedDict()        

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        ret = -1
        if key in self.cache:
            ret = self.cache[key]
            self.cache.move_to_end(key, last = True)
        return ret       
    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.cache[key] = value
        self.cache.move_to_end(key, last = True)
        if len(self.cache) > self.size:
            self.cache.popitem(last = False)
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
