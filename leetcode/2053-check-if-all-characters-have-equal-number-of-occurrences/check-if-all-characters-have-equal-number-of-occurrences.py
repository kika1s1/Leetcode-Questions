class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return True if len(set(Counter((s)).values())) ==1 else False
    