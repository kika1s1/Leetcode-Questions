class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = 1
        inc = True
        for i in range(time):
            if inc and p < n:
                p +=1
            elif not inc and p > 1:
                p -=1
            else:
                if inc:
                    p -=1
                else:
                    p +=1
                inc = not inc
        return p