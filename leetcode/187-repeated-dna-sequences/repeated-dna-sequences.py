class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                res.add(seq)
            seen.add(seq)
        return list(res)
        