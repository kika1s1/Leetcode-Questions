# from collections import Counter
# from itertools import accumulate

# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         remainders = Counter(map(lambda x: x % k, accumulate(nums)))        
#         ans = 0
#         for r in remainders:
#             ans += remainders[r] * (remainders[r]-1) // 2
#         ans += remainders[0]
#         return ans

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=[0 for i in range(k+1)]
        count[0]=1
        res=0
        s=0
        for i in nums:
            s+=i
            s=s%k
            res+=count[s]
            count[s]+=1
        return res