class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        tot = 0
        maxim = 0
        n = len(customers)
        for i in range(n):
            if i < minutes:
                if grumpy[i] == 0:
                    continue
                tot +=customers[i]
                maxim = max(maxim, tot)
            else:
                prev = i - minutes
                if grumpy[prev] ==1:
                    tot -= customers[prev]
                if grumpy[i] ==1:
                    tot +=customers[i]
                maxim = max(maxim, tot)
        satisfied = 0
        for i, j in zip(customers, grumpy):
            if j == 0:
                satisfied +=i
        return maxim + satisfied
                


