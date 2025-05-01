# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        return self.coinChangeRecursive(amount, coins, 0, memo)
    
    def coinChangeRecursive(self, amount: int, coins: List[int], index: int, memo: dict) -> int:
        if amount == 0:
            return 1
        if amount < 0 or index >= len(coins):
            return 0
        
        if (amount, index) in memo:
            return memo[(amount, index)]
        
        count = 0
        count += self.coinChangeRecursive(amount - coins[index], coins, index, memo)
        count += self.coinChangeRecursive(amount, coins, index + 1, memo)
        
        memo[(amount, index)] = count
        return count