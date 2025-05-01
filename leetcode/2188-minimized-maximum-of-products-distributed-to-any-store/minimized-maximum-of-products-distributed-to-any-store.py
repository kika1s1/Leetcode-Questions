class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def possible(x):
            cnt = 0
            for quantitie in quantities:
                if quantitie > x:
                    div = ceil(quantitie/x)
                    cnt +=(div)
                else:
                    cnt +=1
            return cnt <= n and cnt <=(sum(quantities))
        l, r  = 1, max(quantities)
        best = r
        while l <=r:
            mid = (l+r)//2
            if  mid !=0 and possible(mid):
                r = mid-1
                best = mid
            else:
                l = mid + 1
        return best