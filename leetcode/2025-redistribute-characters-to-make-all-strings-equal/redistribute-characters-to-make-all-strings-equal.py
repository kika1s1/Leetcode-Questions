class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        ans=''.join(words)
        res=set(ans)
        for i in res:
            if ans.count(i)%n!=0:
                return False
        return True        