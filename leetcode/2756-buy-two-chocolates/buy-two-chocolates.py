class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        count = 0
        prices.sort()

        return money - (prices[0]+prices[1]) if (prices[0]+prices[1]) <= money else money
            