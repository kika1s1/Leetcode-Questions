class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        
        maxim = word1 if len(word1) > len(word2) else word2
        minim = len(word1) if len(word1) < len(word2) else len(word2)
        o = 0
        e = 0

        for i in range(minim*2):
            if i%2 ==0:
                ans +=word1[e]
                e +=1
            else:
                ans +=word2[o]
                o +=1
        ans +=maxim[o:]
        return ans