class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        ws = len(p)
        p = Counter(p)
        r = ws
        for i in range(len(s)+1-ws):
            sub = s[i:r+i]
            if Counter(sub) == p:
                res.append(i)
        return res
