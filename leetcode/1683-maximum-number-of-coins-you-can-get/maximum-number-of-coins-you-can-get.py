class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        start = len(piles)//3
        while start < len(piles):
            total +=piles[start]
            start +=2
        return total

