class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        for i in s:
            if i in l:
                continue
            else:
                l.append(i)
        return len(l)
