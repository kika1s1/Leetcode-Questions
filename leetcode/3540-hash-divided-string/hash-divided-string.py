class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0, len(s), k):
            sub  = (s[i:i+k])
            tot = 0
            for i in range(len(sub)):
                tot += ord(sub[i])-97
            ans += chr(tot%26 + 97)

        return ans