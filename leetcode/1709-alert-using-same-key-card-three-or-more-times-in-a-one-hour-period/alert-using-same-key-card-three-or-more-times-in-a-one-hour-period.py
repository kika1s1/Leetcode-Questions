from collections import defaultdict
from sortedcontainers import SortedList
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_time = defaultdict(SortedList)
        for name, time in zip(keyName, keyTime):
            minitues = int(time[:2]) * 60 + int(time[3:])
            name_time[name].add(minitues)
        res = []
        print(name_time)

        for name, times in name_time.items():
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    res.append(name)
                    break
        return sorted(res)
