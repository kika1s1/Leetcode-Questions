class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            minim = float("inf")
            for j in range(len(s)):
                if s[j] ==c:
                    minim = min(minim, abs(i-j))
            ans.append(minim)
        return ans

