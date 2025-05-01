class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_s = []
        for i in timeSeries:
            time_s.append(i+duration)
        ans = 0
        for i in range(len(time_s)):
            if i ==0:
                ans +=time_s[i]-timeSeries[i]
            else:
                if timeSeries[i] <= time_s[i-1]:
                    ans +=(time_s[i]- time_s[i-1])
                else:
                    ans +=(time_s[i]- timeSeries[i])
        return ans