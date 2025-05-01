class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indexTable = {}
        minim = float("inf")
        for i, j in enumerate(cards):
            if j not in indexTable:
                indexTable[j] = i
            else:
                minim = min(minim,( i - indexTable[j])+1)
                indexTable[j] = i
        return -1 if minim == float("inf") else minim
            