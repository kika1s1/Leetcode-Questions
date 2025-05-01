class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i in time:
            remainder = i % 60
            complement = (60 - remainder) % 60
            if complement in cnt:
                ans += cnt[complement]
            cnt[remainder] += 1
        return ans
