class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        delta = (sumBob - sumAlice) // 2
        bobSet = set(bobSizes)
        
        for candy in aliceSizes:
            if (candy + delta) in bobSet:
                return [candy, candy + delta]
                