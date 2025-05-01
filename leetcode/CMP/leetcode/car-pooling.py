class Solution:
    def carPooling(self, trips, capacity: int) -> bool:  
        n = len(trips)
        prefix = [0]*(1001)
        left = 1e9
        right = 0
        for tpl in trips:
            prefix[tpl[1]] += tpl[0]
            prefix[tpl[2]] -= tpl[0]
            left = min(left, tpl[1])
            right = max(right, tpl[2])
        
        totalPass = 0
        for i in range(left, right+1):
            totalPass += prefix[i]
            if totalPass > capacity: return False
        return True