class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n=len(s)
        if k>n: return 0
        d=Counter(s)
        valid =True
        i=mx=0

        for j in range(n):
            if d[s[j]]<k:
                mx=max(mx,self.longestSubstring(s[i:j],k))
                i=j+1
                valid=False
        if not valid: return max(mx,self.longestSubstring(s[i:],k)) 
        return n         