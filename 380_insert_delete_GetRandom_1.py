import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here
        """
        self.val_set = set()
        self.val_list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_set:
            return False
        self.val_set.add(val)
        self.val_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.val_set:
            self.val_set.remove(val)
            self.val_list.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.val_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
