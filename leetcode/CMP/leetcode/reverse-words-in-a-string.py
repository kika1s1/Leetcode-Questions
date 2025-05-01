class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        l, r, = 0, len(s)-1
        while l < r:
            s[l],s[r] = s[r], s[l]
            l += 1
            r -= 1
        return " ".join(s)