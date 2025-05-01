class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = [0 for i in range(k+1)]
        cnt[0]  = 1
        res = 0
        s = 0
        for num in nums:
            s +=num
            s = s%k
            res +=cnt[s]
            cnt[s] +=1
        return res