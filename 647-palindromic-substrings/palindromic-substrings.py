class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            l, r = i, i
            # odd
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    ans +=1
                else:
                    break
                l -=1
                r +=1
            l, r = i-1, i
            # even
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    ans +=1
                else:
                    break
                l -=1
                r +=1
        return ans