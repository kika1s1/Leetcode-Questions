class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo = {}
        # def changeCoin(amount, index, memo):
        #     if amount == 0:
        #         return 1
        #     if amount < 0 or index >= len(coins):
        #         return 0
        #     if (amount, index) in memo:
        #         return memo[(amount, index)]
        #     coin = 0
        #     coin +=changeCoin(amount-coins[index], index, memo)
        #     coin +=changeCoin(amount, index + 1, memo)
        #     memo[(amount, index)] = coin
        #     return memo[(amount, index)]
        # return changeCoin(amount, 0, memo)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(amount-c+1):
                dp[c+i] +=dp[i]
        return dp[amount]