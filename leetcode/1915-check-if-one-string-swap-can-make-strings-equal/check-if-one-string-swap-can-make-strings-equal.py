class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        cnt = 0
        for a, b in zip(s1, s2):
            if a !=b:
                cnt +=1
        return cnt <= 2