class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim = 0
        minim =  prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minim:
                minim = prices[i]
            maxim = max(maxim, prices[i]-minim)
        return maxim
            
            

