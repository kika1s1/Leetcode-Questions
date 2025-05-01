class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ws = len(s1)
        s1 = "".join(sorted(list(s1)))
        loop = (len(s2)-ws)+1
        for i in range(loop):
            sub = "".join(sorted(list(s2[i:ws+i])))
            if sub == s1:
                return True
        return False