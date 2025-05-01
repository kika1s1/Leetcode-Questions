class Solution:
    def minOperations(self, s: str) -> int:
        change_1 = 0
        cur = True

        for c in s:
            if cur == (c == "0"):
                change_1 += 1
            
            cur = not cur
        return min(change_1, len(s) - change_1)