# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = 0
        for price in prices:
            if start > price:
                start = price 
            else:
                profit = max(profit, price-start)
        return profit