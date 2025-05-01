from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePointInMinutes = []
        
        for time in timePoints:
            hour, minute = map(int, time.split(":"))
            minutes = hour * 60 + minute
            timePointInMinutes.append(minutes)
        
        timePointInMinutes.sort()
        
        minim = float("inf")
        
        for i in range(1, len(timePointInMinutes)):
            minim = min(minim, timePointInMinutes[i] - timePointInMinutes[i - 1])
        
        minim = min(minim, (24 * 60 - timePointInMinutes[-1] + timePointInMinutes[0]))
        
        return minim
