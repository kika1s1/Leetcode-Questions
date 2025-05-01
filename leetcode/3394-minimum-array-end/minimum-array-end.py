class Solution:
    def minEnd(self, n: int, x: int) -> int:
        b=1
        n-=1
        ret=x
        while n:
            if b&x==0:
                if n&1:
                    ret|=b
                n //=2
            b *=2
        return ret
        