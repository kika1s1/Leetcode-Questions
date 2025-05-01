s = [1, 2, 2]
i = 2
while len(s) <= 10**5:
    s+=[3-s[-1]]*s[i]
    i+=1
class Solution:
    def magicalString(self, n: int) -> int:
        return s[:n].count(1)