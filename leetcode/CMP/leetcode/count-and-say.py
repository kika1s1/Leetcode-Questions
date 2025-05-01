class Solution:
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        c = 0
        digit = s[0]
        ret = []
        for i in range(len(s)):
            if s[i] == digit:
                c += 1
            else:
                ret.append(str(c) + digit)
                c = 1
                digit = s[i]
        ret.append(str(c) + digit)
        return "".join(ret)