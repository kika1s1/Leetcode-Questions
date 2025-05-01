class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rep = Counter()
        for num in arr:
            mod = num % k
            if mod == 0:
                if mod  in rep:
                    rep[mod] -=1
                    if rep[mod] == 0:
                        del rep[mod]
                else:
                    rep[mod] +=1
            else:
                diff = k - mod
                if diff in rep:
                    rep[diff] -=1
                    if rep[diff] == 0:
                        del rep[diff]
                else:
                    rep[mod] +=1
        return True if len(rep) == 0 else False
                