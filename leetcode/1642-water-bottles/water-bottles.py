class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            left  = numBottles % numExchange
            drink = numBottles//numExchange
            ans +=drink
            numBottles = left + drink
        return ans