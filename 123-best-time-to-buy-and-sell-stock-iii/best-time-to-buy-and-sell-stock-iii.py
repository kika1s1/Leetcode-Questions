class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f_buy, f_sell = -prices[0], 0
        s_buy, s_sell = -prices[0], 0
        for price in prices[1:]:
            f_buy = max(f_buy, -price)
            f_sell = max(f_sell, f_buy + price)
            s_buy = max(s_buy, f_sell - price)
            s_sell = max(s_sell, s_buy + price)
        return s_sell