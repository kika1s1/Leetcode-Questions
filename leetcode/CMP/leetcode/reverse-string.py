class Solution(object):
    def reverseString(self, s):
        def helper(start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            helper(start + 1, end - 1)

        helper(0, len(s) - 1)
        return s