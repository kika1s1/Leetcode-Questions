class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        cnt = Counter(stones)
        for char in jewels:
            ans +=cnt[char]
        return ans