class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        num = s.count(c)

        res = num * (num - 1) // 2 + num
        return res