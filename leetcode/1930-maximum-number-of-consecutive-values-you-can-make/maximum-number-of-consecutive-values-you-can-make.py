class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_reachable = 0
        
        for coin in coins:
            if coin > max_reachable + 1:
                break
            max_reachable += coin
        return max_reachable + 1
