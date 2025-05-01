class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        maxim = 1
        l_s = len(s)
        l_t = len(t)
        for i in range(l_s+1):
            for j in range(i, l_s+1):
                sub = s[i:j+1]
                for a in range(l_t+1):
                    for b in range(a, l_t+1):
                        s_sub = t[a:b+1]
                        conc = sub + s_sub
                        if conc[::-1] == conc:
                            maxim = max(maxim, len(conc))
        return maxim
