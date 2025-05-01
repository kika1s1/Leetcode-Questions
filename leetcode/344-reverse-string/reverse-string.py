class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(l, r):
            if l > r:
                return s
            s[l], s[r] = s[r], s[l]
            return reverse(l+1, r -1)
        return reverse(0, len(s)-1)