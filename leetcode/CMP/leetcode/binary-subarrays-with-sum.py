class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        res = 0
        temp = 0
        d = {0:1}

        for n in nums:
            temp += n
            if temp - k in d:
                res += d[temp-k]
            d[temp] = d.get(temp, 0) + 1
        return res