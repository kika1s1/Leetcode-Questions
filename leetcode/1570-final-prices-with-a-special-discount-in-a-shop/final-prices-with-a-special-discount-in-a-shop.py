class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            index = i
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    index = j
                    break
            if index == i:
                ans.append(prices[index])
            else:
                ans.append(prices[i] - prices[index])
        return ans