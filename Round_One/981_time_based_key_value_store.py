class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_table[key].append([timestamp,value])

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_table or timestamp < self.hash_table[key][0][0]:
            return ""
        elif timestamp > self.hash_table[key][-1][0]:
            return self.hash_table[key][-1][1]
        
        low, high = 0 , len(self.hash_table[key]) - 1
        
        while low <= high:
            mid  = (low+high)//2
            if self.hash_table[key][mid][0] == timestamp:
                return self.hash_table[key][mid][1]
            elif self.hash_table[key][mid][0] >= timestamp:
                high = mid -1
            else:
                low = mid + 1
        
        return self.hash_table[key][high][1]
        
        
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)