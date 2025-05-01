class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i in hours:
            remainder = i % 24
            complement = (24 - remainder) % 24
            if complement in cnt:
                ans += cnt[complement]
            cnt[remainder] += 1
        return ans

