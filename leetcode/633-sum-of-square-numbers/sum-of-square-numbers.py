class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(sqrt(c))
        while l <=r:
            if l*l + r*r == c:
                return True
            elif l *l + r*r < c:
                l +=1
            else:
                r -=1
        return False