class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashIndex = {}
        for i, j in enumerate(s):
            hashIndex[j] = i
        summation = 0
        for i, j in enumerate(t):
            summation +=abs(i-hashIndex[j])
        return summation