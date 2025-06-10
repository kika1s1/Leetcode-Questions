class Solution:
    def maxDifference(self, s: str) -> int:
        ans = 0
        maxim_odd = 0
        minim_even = float("inf")
        rep_count = Counter(s)
        for char, rep in rep_count.items():
            if rep % 2 == 0:
                minim_even = min(minim_even, rep)
            else:
                maxim_odd = max(maxim_odd, rep)
        return maxim_odd - minim_even