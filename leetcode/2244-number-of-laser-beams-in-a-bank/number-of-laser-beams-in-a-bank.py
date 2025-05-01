class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        prev=0
        for i in bank:
            res=i.count('1')
            if res:
                ans+=prev*res
                prev=res
        return ans        