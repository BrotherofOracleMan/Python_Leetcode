from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.h_t = defaultdict(int)
        
    def add(self, number: int) -> None:
        self.h_t[number] += 1
        
    def find(self, value: int) -> bool:
        for key in self.h_t.keys():
            if value - key in self.h_t:
                complement = value - key
                if complement != key:
                    return True
                elif self.h_t[complement] > 1:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
