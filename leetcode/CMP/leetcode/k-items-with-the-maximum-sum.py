class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        rem = k - numOnes - numZeros
        if rem <= 0:
            return numOnes
        return numOnes - rem