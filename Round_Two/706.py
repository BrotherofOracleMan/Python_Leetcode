class Bucket():
    def __init__(self):
        self.values = []

    def put(self, key, value):
        index = -1
        for i in range(len(self.values)):
            if self.values[i][0] == key:
                index = i
                self.values[index][1] = value
                break
        if index == -1: self.values.append([key,value])

    def get(self,key):
        for entry in self.values:
            if entry[0] == key:
                return entry[1]
        return -1   
    def remove(self, key):
        index = -1
        for i in range(len(self.values)):
            if self.values[i][0] == key:
                index = i
        if index != -1: del self.values[index]  



class MyHashMap:
    def __init__(self):
        self.n = 1069
        self.bucket_list = [Bucket()] * self.n 

    def put(self, key: int, value: int) -> None:
        self.bucket_list[key%self.n].put(key,value)

    def get(self, key: int) -> int:
        return self.bucket_list[key%self.n].get(key)

    def remove(self, key: int) -> None:
        return self.bucket_list[key%self.n].remove(key)

        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
