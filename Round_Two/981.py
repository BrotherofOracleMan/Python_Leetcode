from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timemap = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        arr = self.timemap[key]
        if timestamp >= arr[-1][0]:
            return arr[-1][1]
        if arr[0][0] > timestamp:
            return ""
        if arr[0][0] == timestamp:
            return arr[0][1]
        low , high = 0, len(arr) -1

        while low <= high:
            mid = low + (high - low)//2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] >= timestamp:
                high = mid - 1
            else:
                low = mid + 1
        return arr[high][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
