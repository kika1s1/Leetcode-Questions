class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = x
        t = 0

        while n > 9:
            r = x%10
            n = n//10
            
            t +=r
        t +=n
        return t if x%t == 0 else -1
        
