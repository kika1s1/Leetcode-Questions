class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashIndex = {}
        for i, chr in enumerate(order):
            hashIndex[chr] = i
    
        
        ans = []
        for i in range(len(words)):
            pos = []
            for chr in words[i]:
                pos.append(hashIndex[chr])
            ans.append(pos)
        sortedV = sorted(ans)
        if ans == sortedV:
            return True
        else:
            return False

        