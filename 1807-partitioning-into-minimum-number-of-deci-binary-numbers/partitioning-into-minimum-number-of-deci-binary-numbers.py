class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for char in n:
            ans = max(ans, int(char))
        return ans