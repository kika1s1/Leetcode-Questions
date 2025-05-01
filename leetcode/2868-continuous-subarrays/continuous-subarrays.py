class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i = res = 0
        d = dict()
        for j, num in enumerate(nums):
            t = d.copy()
            for k, v in t.items():
                if abs(k - num) > 2:
                    i = max(i, v + 1)
                    d.pop(k)
            d[num] = j
            res += j - i + 1
        return res