class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [x for x in s]
        for i, j in zip(indices, s):
            ans[i] = j
        return "".join(ans)