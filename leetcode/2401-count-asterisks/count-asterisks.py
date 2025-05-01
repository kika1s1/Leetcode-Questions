class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        bar = 0
        for i in s:
            
            if i == "|":
                bar +=1
            elif bar % 2 == 0 and i == "*":
                cnt +=1
        return cnt
            
            
