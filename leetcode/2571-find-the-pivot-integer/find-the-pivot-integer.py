class Solution:
    def pivotInteger(self, n: int) -> int:
        
        s=(n*(n+1))/2
        p=int(s**0.5)
        k=(p*(p+1))/2
        if s+p-k==k:
            return p
        else:
            return -1
        