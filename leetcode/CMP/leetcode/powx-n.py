class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        if n<0:
            x=1/x
            n=-n
        while n:
            if n%2==1:
                res*=x
            x*=x
            n//=2
        return res
        