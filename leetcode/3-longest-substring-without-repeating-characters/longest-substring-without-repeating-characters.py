class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        Cnt = Counter()
        N = len(s)
        maxim = float("-inf")
        for right in range(N):
            if s[right] not in Cnt:
                maxim = max(maxim,  (right - left +1))
                Cnt[s[right]] +=1
            else:
                while s[left] != s[right]:
                    if Cnt[s[left]] ==1:
                        del Cnt[s[left]]
                    else:
                        Cnt[s[left]] -=1
                    left +=1
                left +=1
        return 0 if maxim == float("-inf") else maxim


