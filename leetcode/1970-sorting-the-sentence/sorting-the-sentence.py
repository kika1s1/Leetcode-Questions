class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split()
        for i in s.split():
            place = int(i[-1])-1
            ans[place] = i[:-1]
        return " ".join(ans)