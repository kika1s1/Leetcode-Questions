from bisect import bisect_right
from collections import defaultdict
from sortedcontainers import SortedList

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].add([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        idx = bisect_right(self.time_map[key], [timestamp, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"]) - 1
        if idx >= 0:
            return self.time_map[key][idx][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)