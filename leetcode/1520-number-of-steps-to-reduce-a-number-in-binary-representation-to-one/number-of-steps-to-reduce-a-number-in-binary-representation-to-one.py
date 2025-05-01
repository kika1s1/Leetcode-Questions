class Solution:
    def numSteps(self, s: str) -> int:
        ans, car = 0, False

        for b in s[1:][::-1]:
            if (b == "1" and not car )or( b == "0" and car):
                ans += 2
                car = True
            else: 
                ans += 1
        return ans + int(car)