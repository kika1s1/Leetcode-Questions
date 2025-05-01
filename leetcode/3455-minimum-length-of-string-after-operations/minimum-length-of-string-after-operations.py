class Solution:
    def minimumLength(self, s: str) -> int:
        rep = Counter(s)
        ans = 0
        for key, value in rep.items():
            if value %2 ==0:
                ans +=2
            else:
                ans +=1
        return ans