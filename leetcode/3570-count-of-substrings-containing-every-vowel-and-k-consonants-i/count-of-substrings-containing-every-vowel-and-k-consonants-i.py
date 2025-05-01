class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def checkCnt(sub, k):
            vowel = {"a", "e", "i", "o", "u"}
            visited = set()
            cntV = 0
            cntC = 0
            for a in sub:
                if a in vowel and a not in visited:
                    cntV +=1
                    visited.add(a)
                elif a not in vowel:
                    cntC +=1
                    visited.add(a)
            return cntV == 5 and cntC == k



        N = len(word)
        S = k+5
        cnt = 0
        for i in range(N):
            for j in range(i, N-S+1):
                sub = word[i:j+S]
                cnt +=checkCnt(sub, k)

        return cnt