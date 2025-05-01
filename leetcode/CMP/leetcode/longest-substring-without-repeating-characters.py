class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 2
        if len(s) < 2:
            return len(s)
        maxim = 0
        while r <=len(s):
            sub = s[l:r]
            if len(sub) == len(set(sub)):
                maxim = max(maxim, len(sub))
                r +=1
                if len(sub) == len(set(sub)):
                    maxim = max(maxim, len(sub))
                else:
                    l+=1
                maxim = max(maxim, len(sub))
            else:
                l +=1

        return maxim
            
                
