class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashMap = {}
        scored = sorted(score, reverse=True)
        for i, j in enumerate(scored):
            if i ==0:
                hashMap[j] ="Gold Medal"
            elif i == 1:
                hashMap[j] ="Silver Medal"
            elif i ==2:
                hashMap[j] ="Bronze Medal"
            else:
                hashMap[j] = str(i +1)
        ans = []
        for i in score:
            ans.append(hashMap[i])
        return ans

