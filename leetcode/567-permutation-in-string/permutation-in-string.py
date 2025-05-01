class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:len(s1)])  
        if cnt1 == cnt2:
            return True
        for i in range(len(s1), len(s2)):
            cnt2[s2[i]] += 1  
            cnt2[s2[i - len(s1)]] -= 1  
            if cnt2[s2[i - len(s1)]] == 0:
                del cnt2[s2[i - len(s1)]]
            if cnt1 == cnt2:
                return True
        return False
