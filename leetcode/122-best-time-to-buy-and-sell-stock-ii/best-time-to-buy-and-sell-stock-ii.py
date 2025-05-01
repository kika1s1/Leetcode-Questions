class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        @cache
        def dp(index, holding):
            if index == N:
                return 0
            if not holding:
                buy = dp(index + 1, True) - prices[index]
                skip = dp(index + 1, False)
                return max(buy, skip)

            else:
                sell = dp(index + 1, False) + prices[index]
                skip = dp(index + 1, True)
                return max(sell, skip)
        return dp(0, False)
