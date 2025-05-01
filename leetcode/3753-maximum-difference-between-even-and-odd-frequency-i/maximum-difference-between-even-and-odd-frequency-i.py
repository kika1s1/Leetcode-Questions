class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd = float("-inf")
        even = float("inf")
        for char, rep in cnt.items():
            if rep %2 == 0:
                even = min(even, rep)
            else:
                odd = max(odd, rep)
        return odd - even