class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        cnt_rep = Counter(p)
        k = len(p)
        sub  = Counter()
        for i in range(k):
            sub[s[i]] +=1
        ans = []
        if sub == cnt_rep:
            ans.append(0)
        for i in range(k, len(s)):
            sub[s[i]] +=1
            if sub[s[i-k]] > 1:
                sub[s[i-k]]  -=1
            else:
                del sub[s[i-k]] 
            if sub == cnt_rep:
                ans.append(i-k+1)
        return ans

