class Solution:
    def maximumLength(self, s: str) -> int:
        def possible(mid):
            rep = Counter()
            for i in range(len(s) - mid + 1):
                sub = s[i:i + mid]
                if len(set(sub)) == 1:
                    rep[sub] += 1
                    if rep[sub] >= 3: 
                        return True
            return False

        l, r, best = 1, len(s), -1
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        return best
