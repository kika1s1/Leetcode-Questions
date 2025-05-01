class Solution:
    def maxIceCream(self, costs, coins):
        costs.sort()
        cnt = 0
        for i in costs:
            if i > coins:
                return cnt
            coins -= i
            cnt += 1
        return cnt
#read kind of easy