class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            cnt = 0
            while i:
                cnt +=(i & 1)
                i >>=1
            ans.append(cnt)
        return ans