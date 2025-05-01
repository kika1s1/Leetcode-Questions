class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sumArr = []
        for i in range(1, len(weights)):
            sumArr.append(weights[i] + weights[i-1])
        sumArr.sort()
        maxim = 0
        minim = 0
        n = len(weights)
        for i in range(k-1):
            minim +=sumArr[i]
            maxim +=sumArr[n-i-2]
        return maxim - minim
