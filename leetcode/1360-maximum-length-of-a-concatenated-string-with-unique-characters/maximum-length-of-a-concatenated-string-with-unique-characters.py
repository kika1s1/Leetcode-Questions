class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        res = [""]
        op = 0
        
        for word in arr:
            for r in res:
                newRes = r+word
                if len(newRes)!=len(set(newRes)): continue
                res.append(newRes)
                op = max(op, len(newRes))
        return op