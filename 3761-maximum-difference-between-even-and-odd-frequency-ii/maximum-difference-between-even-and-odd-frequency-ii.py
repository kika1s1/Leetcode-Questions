class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ans = -inf
        for a in "01234": 
            for b in "01234": 
                if a != b: 
                    seen = defaultdict(lambda : inf)
                    pa = [0]
                    pb = [0]
                    ii = 0 
                    for i, ch in enumerate(s): 
                        pa.append(pa[-1])
                        pb.append(pb[-1])
                        if ch == a: pa[-1] += 1
                        elif ch == b: pb[-1] += 1
                        while ii <= i-k+1 and pa[ii] < pa[-1] and pb[ii] < pb[-1]: 
                            key = (pa[ii] % 2, pb[ii] % 2) 
                            diff = pa[ii] - pb[ii]
                            seen[key] = min(seen[key], diff)
                            ii += 1
                        key = (1 - pa[-1] % 2, pb[-1] % 2) 
                        diff = pa[-1] - pb[-1]
                        ans = max(ans, diff - seen[key])
        return ans 