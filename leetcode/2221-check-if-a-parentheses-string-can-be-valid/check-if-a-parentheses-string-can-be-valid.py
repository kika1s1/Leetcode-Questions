class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        open_count = 0
        for i in range(len(s)):
            if s[i] == "(" or locked[i] == "0":
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")" or locked[i] == "0":
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
        return True
