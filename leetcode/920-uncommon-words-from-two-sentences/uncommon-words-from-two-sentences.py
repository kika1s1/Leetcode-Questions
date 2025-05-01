class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split(" "))
        s2 = Counter(s2.split(" "))
        ans = []
        for s in s1:
            if s1[s] ==1 and s not in s2:
                ans.append(s)
        
        for s in s2:
            if s2[s] ==1 and s not in s1:
                ans.append(s)
        return ans
        