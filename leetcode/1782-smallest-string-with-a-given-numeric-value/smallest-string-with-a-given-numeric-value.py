class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for i in range(n):
            ans.append(26)
        total = sum(ans)
        dec = total - k
        for i in range(len(ans)):
            if dec >= 26:
                ans[i] -=25
                dec -= 25
            else:
                ans[i] -=dec
                dec -= dec
        for i in range(len(ans)):
            ans[i] = chr(96+ans[i])
        return "".join(ans)