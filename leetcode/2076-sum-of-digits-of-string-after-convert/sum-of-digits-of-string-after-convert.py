class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for i in s:
            num +=str(ord(i)-ord("a")+1)
        N = len(num)
        for i in range(k):
            ans = 0
            for j in range(len(num)):
                ans +=int(num[j])
            num = str(ans)
        return ans


