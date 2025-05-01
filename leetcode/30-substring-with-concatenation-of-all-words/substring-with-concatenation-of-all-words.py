class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        N = len(words)*len(words[0])
        size = len(words[0])
        S = len(s)
        l = 0
        ans = []
        for r in range(S-N+1):
            sub = s[l+r:N+r]
            pos  = []
            left = l+r
            for i in range(left,N+r, size):
                word = s[i:size+i]
                pos.append(word)
            if sorted(pos) ==words:
                ans.append(l+r)
        return ans
