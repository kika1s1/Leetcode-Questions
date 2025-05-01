class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = [Counter(word) for word in words]
        ans = []
        for alphabet in cnt[0]:
            isExist  = True
            minim = float("inf")
            for i in range(len(words)):
                if alphabet not in cnt[i]:
                    isExist = False
                else:
                    minim = min(minim, cnt[i][alphabet])
            if isExist:
                for i in range(minim):
                    ans.append(alphabet)
        return ans





        