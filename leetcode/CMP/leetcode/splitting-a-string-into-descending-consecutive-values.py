class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start, prev):
            for i in range(start, len(s) - 1):
                split = int(s[start: i + 1])
                if prev == -1 or prev-1 == split:
                    if backtrack(i+1, split):
                      return  True
            if prev != -1 and int(s[start:]) == prev - 1:
                return True
            return False
        return backtrack(0, -1)