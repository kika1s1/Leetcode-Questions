class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            m = lo + (hi - lo >> 1)
            cur = arr[m]
            if cur - m - 1 < k:
                lo = m + 1
            else:
                hi = m
        return hi + k