class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        r = 1
        while r < len(s):
            left = s[:r]
            right = s[r:]
            total = left.count("0") + right.count("1")
            if total > maximum:
                maximum = total
            r +=1
        return maximum

        